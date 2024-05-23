#######################################################################
#  TARDIS - Transformer And Rapid Dimensionless Instance Segmentation #
#                                                                     #
#  New York Structural Biology Center                                 #
#  Simons Machine Learning Center                                     #
#                                                                     #
#  Robert Kiewisz, Tristan Bepler                                     #
#  MIT License 2021 - 2024                                            #
#######################################################################
from typing import Optional, Tuple, Union

import numpy as np
from scipy.interpolate import splev, splprep
from scipy.spatial.distance import cdist
from sklearn.neighbors import KDTree

from tardis_em.dist_pytorch.utils.utils import pc_median_dist
from tardis_em.utils.errors import TardisError


def resample_filament(points, spacing_size):
    """
    Resamples points for each filament so they have the given spacing size.

    Parameters:
    points (np.array): Array of shape [N, 4] where each column is [ID, X, Y, Z].
    spacing_size (float): Desired spacing size between points.

    Returns:
    np.array: Resampled array with the same structure.
    """
    unique_ids = np.unique(points[:, 0])
    resampled_points = []

    for filament_id in unique_ids:
        filament_points = points[points[:, 0] == filament_id][:, 1:]
        if filament_points.shape[0] < 2:
            resampled_points.append(points[points[:, 0] == filament_id])
            continue

        cumulative_distances = np.cumsum(np.sqrt(np.sum(np.diff(filament_points, axis=0) ** 2, axis=1)))
        cumulative_distances = np.insert(cumulative_distances, 0, 0)

        num_new_points = int(cumulative_distances[-1] // spacing_size)
        new_points = [filament_points[0]]

        for i in range(1, num_new_points + 1):
            target_distance = i * spacing_size
            idx = np.searchsorted(cumulative_distances, target_distance)
            if idx >= len(cumulative_distances):
                continue

            if cumulative_distances[idx] == target_distance:
                new_points.append(filament_points[idx])
            else:
                ratio = (target_distance - cumulative_distances[idx - 1]) / (
                            cumulative_distances[idx] - cumulative_distances[idx - 1])
                new_point = filament_points[idx - 1] + ratio * (filament_points[idx] - filament_points[idx - 1])
                new_points.append(new_point)

        new_points = np.array(new_points)
        filament_ids = np.full((new_points.shape[0], 1), filament_id)
        resampled_points.append(np.hstack((filament_ids, new_points)))

    return np.vstack(resampled_points)


class FilterConnectedNearSegments:
    """
    Connect splines based on spline trajectory and splines end distances.
    """

    def __init__(self, distance_th=1000, cylinder_radius=150):
        """
        Initialize the class with the distance threshold and cylinder radius parameters.

        Args:
            distance_th (int): Maximum distance between two spline endpoints for them
            to be considered for merging.
            cylinder_radius (int): Maximum distance between spline endpoint and the line
            connecting its neighboring endpoints for them to be considered for merging.
        """
        self.distance_th = distance_th
        self.cylinder_radius = cylinder_radius

    @staticmethod
    def _in_cylinder(point: np.ndarray, axis: tuple, r: int, h: int) -> bool:
        """
        Fast check if point is inside a cylinder by projecting point on cylinder
        volume in 3D.

        Args:
            point (np.ndarray): Point in 3D to project on cylinder.
            axis (tuple): Cylinder axis of orientation.
            r (int): Cylinder radius.
            h (int): Cylinder length.

        Returns:
            bool: If True, given point can be found in a cylinder.
        """
        # project the point onto the axis
        ax1 = (point - axis[0]) + 1e-16
        ax2 = (axis[1] - axis[0]) + 1e-16

        d = np.dot(ax1, ax2) / np.linalg.norm(ax2)

        # check if d is within the range [0, h]
        if d < 0 or d > h:
            return False

        # calculate the perpendicular distance
        d = np.linalg.norm(ax1 - d * (ax2) / np.linalg.norm(ax2))

        # check if d is less than the radius
        return d <= r

    @staticmethod
    def _remove_duplicates(d: dict) -> dict:
        """
        Remove duplicate splines

        Args:
            d (dict): Dictionary containing splines.

        Returns:
            dict: dictionary containing unique splines.
        """
        new_d = {}
        [
            new_d.update({k: v.tolist()})
            for k, v in d.items()
            if v.tolist() not in new_d.values()
        ]

        return new_d

    def splines_direction(self, spline1: list, spline2: list) -> bool:
        """
        Check if two splines facing the same direction. Knowing that spline1 facing
        a direction of spline2, check if spline2 also face a direction of spline1.

        Args:
            spline1 (list): Sorted array of point with 3D coordinates.
            spline2 (list): Sorted array of point with 3D coordinates.

        Returns:
            bool: If true, given splines facing the same direction
        """
        # Check 01 - 01 & Check 01 - 10
        ax = [
            (np.array(spline2[1]), np.array(spline2[0])),
            (np.array(spline2[1]), np.array(spline2[0])),
        ]
        points = [np.array(spline1[0]), np.array(spline1[-1])]
        s201_s101, s201_s110 = [
            self._in_cylinder(
                point=p, axis=a, r=self.cylinder_radius, h=self.distance_th
            )
            for p, a in zip(points, ax)
        ]

        # Check 10 - 01 and Check 10 - 10
        ax = [
            (np.array(spline2[-2]), np.array(spline2[-1])),
            (np.array(spline2[-2]), np.array(spline2[-1])),
        ]
        points = [np.array(spline1[0]), np.array(spline1[-1])]
        s210_s101, s210_s110 = [
            self._in_cylinder(
                point=p, axis=a, r=self.cylinder_radius, h=self.distance_th
            )
            for p, a in zip(points, ax)
        ]

        # Check if splines facing same direction in any way
        return np.any((s201_s101, s201_s110, s210_s101, s210_s110))

    def marge_splines(
        self, point_cloud: np.ndarray, omit_border: int, initial: bool
    ) -> np.ndarray:
        """
        Connect splines in the point_cloud that are close enough to each other
         and return the reordered splines.

        Example:
            - Get dictionary with {id: [sorted list of points]}

            - While there is more than 1 spline in the dict:
                - Pick first spline in a dict.
                - Select all ends
                - Calc. end distance to all other ends.

                - If any ends within threshold distance:
                    - Calculate initial end vector
                    - Calculate distance to the cylinder

                    - If any picked ends are within cylinder radius
                        - Pick one with the smallest distance
                        - Save two spline IDs to connected

                - If Connected ID list not empty:
                    - Marge and sort points from two IDs
                    - Check tortuosity

                    - If tortuosity <= 1.5:
                        - Add to the connected dict
                        - Remove from dict
                        - start over

                - If connected ID list is empty or tortuosity > 1.5:
                    - Add only initial spline to the connected dict
                    - Remove from dict
                    - start over

        Args:
            point_cloud (np.ndarray): Array with segmented and sorted point cloud
                of a shape [ID, X, Y, Z].
            omit_border (int): In A, distance from the border as a limit not to
                connect splines.
            initial (bool): Initial run for the operation.

        Returns:
            np.ndarray: Array of segmented point cloud with connected splines
            that fit the criteria
        """
        # Find Z bordered to filter out MT connection at the borders
        MIN_Z, MAX_Z = np.min(point_cloud[:, 3]), np.max(point_cloud[:, 3])

        # Create a dictionary to store spline information
        # Iterate through the point cloud and add points to their respective splines
        if initial:
            splines_list_df = {}
            for point in point_cloud:
                id_, x, y, z = point
                if id_ not in splines_list_df:
                    splines_list_df[id_] = []
                splines_list_df[id_].append([x, y, z])

            splines_list = {}
            for i in splines_list_df:
                value = splines_list_df[i]
                if len(value) > 5:
                    splines_list[i] = value
        else:
            splines_list = {}
            for point in point_cloud:
                id_, x, y, z = point
                if id_ not in splines_list:
                    splines_list[id_] = []
                splines_list[id_].append([x, y, z])

        # Iterate throw every spline in the list
        merge_splines = {}
        spline_id = 0
        while len(splines_list) > 1:
            key = list(splines_list.keys())[0]
            value = splines_list[key]  # Pick first spline in the dictionary
            end01 = value[0]
            end10 = value[-1]

            end01_list = [list(x)[1][0] for x in splines_list.items()]
            end10_list = [list(x)[1][-1] for x in splines_list.items()]

            # Check if any ends is within threshold distance
            end01_list01 = np.sqrt(
                np.sum((np.asarray(end01_list) - np.asarray(end01)) ** 2, axis=1)
            )
            end01_list01 = [
                {id_: dist}
                for id_, dist in zip(list(splines_list.keys()), end01_list01)
                if dist <= 1000 and id_ != key
            ]
            end01_list10 = np.sqrt(
                np.sum((np.asarray(end10_list) - np.asarray(end01)) ** 2, axis=1)
            )
            end01_list10 = [
                {id_: dist}
                for id_, dist in zip(list(splines_list.keys()), end01_list10)
                if dist <= self.distance_th and id_ != key
            ]
            end10_list01 = np.sqrt(
                np.sum((np.asarray(end01_list) - np.asarray(end10)) ** 2, axis=1)
            )
            end10_list01 = [
                {id_: dist}
                for id_, dist in zip(list(splines_list.keys()), end10_list01)
                if dist <= self.distance_th and id_ != key
            ]
            end10_list10 = np.sqrt(
                np.sum((np.asarray(end10_list) - np.asarray(end10)) ** 2, axis=1)
            )
            end10_list10 = [
                {id_: dist}
                for id_, dist in zip(list(splines_list.keys()), end10_list10)
                if dist <= self.distance_th and id_ != key
            ]

            # Check if any of the point is within the cylinder and get the closest one
            splines_to_merge = []
            end_lists = [end01_list01, end01_list10, end10_list01, end10_list10]

            for end_list in end_lists:
                for i in end_list:
                    m_id = list(i.keys())[
                        -1 if end_list in [end10_list01, end10_list10] else 0
                    ]
                    m_end = list(splines_list[m_id])

                    not_at_the_border = np.all(
                        [
                            (
                                m_end[
                                    (
                                        -1
                                        if end_list in [end10_list01, end10_list10]
                                        else 0
                                    )
                                ][2]
                                - MIN_Z
                            )
                            >= omit_border,
                            (
                                MAX_Z
                                - m_end[
                                    (
                                        -1
                                        if end_list in [end10_list01, end10_list10]
                                        else 0
                                    )
                                ][2]
                            )
                            >= omit_border,
                        ]
                    )

                    if not_at_the_border:
                        points = np.array(
                            m_end[-1 if end_list in [end10_list01, end10_list10] else 0]
                        )
                        axis = (
                            np.array(
                                value[
                                    (
                                        -2
                                        if end_list in [end10_list01, end10_list10]
                                        else 1
                                    )
                                ]
                            ),
                            np.array(
                                value[
                                    (
                                        -1
                                        if end_list in [end10_list01, end10_list10]
                                        else 0
                                    )
                                ]
                            ),
                        )

                        in_cylinder = self._in_cylinder(
                            point=points,
                            axis=axis,
                            r=self.cylinder_radius,
                            h=self.distance_th,
                        )
                        if in_cylinder:
                            splines_to_merge.append([m_id, m_end])

            # Check if any ends fit criteria for connection
            if len(splines_to_merge) == 1:  # Merge
                # Check if selected spline facing the same direction
                same_direction = self.splines_direction(value, splines_to_merge[0][1])

                # Connect splines
                if same_direction:
                    merged_spline = np.concatenate((value, splines_to_merge[0][1]))
                    merge_splines[spline_id] = sort_segment(merged_spline)

                    del splines_list[splines_to_merge[0][0]]
            elif len(splines_to_merge) > 1:  # If more than one find best
                if len(np.unique([x[0] for x in splines_to_merge])) == 1:
                    # Check if selected spline facing the same direction
                    same_direction = self.splines_direction(
                        value, splines_to_merge[0][1]
                    )

                    # Connect splines
                    if same_direction:
                        merged_spline = np.concatenate((value, splines_to_merge[0][1]))

                        merge_splines[spline_id] = sort_segment(merged_spline)
                        del splines_list[splines_to_merge[0][0]]
                else:
                    end_lists = {}
                    for d in np.concatenate(
                        [end01_list01, end01_list10, end10_list01, end10_list10]
                    ):
                        end_lists.update(d)

                    # Check which splines facing the same direction
                    same_direction = []
                    for d in end_lists:
                        same_direction.append(
                            self.splines_direction(value, splines_list[d])
                        )

                    # Pick splines with the smallest distance that facing same direction
                    end_lists_id = [x for x, b in zip(end_lists, same_direction) if b]
                    same_direction = np.any(same_direction)

                    if len(end_lists_id) > 0:
                        end_lists_id = min(end_lists_id, key=lambda x: end_lists[x])
                        merged_spline = np.concatenate(
                            (value, splines_list[end_lists_id])
                        )

                        merge_splines[spline_id] = sort_segment(merged_spline)
                        del splines_list[end_lists_id]
            else:  # No merge found
                same_direction = True
                merge_splines[spline_id] = sort_segment(value)

            if not same_direction:
                merge_splines[spline_id] = sort_segment(value)

            del splines_list[key]
            spline_id += 1

        # Add last spline to the new list
        try:
            key = list(splines_list.keys())[0]
            merge_splines[spline_id] = splines_list[key]
        except IndexError:
            pass

        return np.concatenate(
            [
                np.hstack((np.repeat(id_, len(array)).reshape(-1, 1), array))
                for id_, array in merge_splines.items()
            ]
        )

    def __call__(self, point_cloud: np.ndarray, omit_border=0):
        past_l = 0
        while len(np.unique(point_cloud[:, 0])) != past_l:
            if past_l == 0:
                past_l = len(np.unique(point_cloud[:, 0]))
                point_cloud = self.marge_splines(
                    point_cloud=point_cloud, omit_border=omit_border, initial=True
                )
            else:
                past_l = len(np.unique(point_cloud[:, 0]))
                point_cloud = self.marge_splines(
                    point_cloud=point_cloud, omit_border=omit_border, initial=False
                )
        return point_cloud


class FilterSpatialGraph:
    """
    Calculate length of each spline and distance between all splines ends.

    This clas iterate over all splines in array [ID, X, Y, Z] by given ID.
    Firstly if specified during initialization, class calculate distance
    between all splines ends and use it to define which splines are obviously
    broken.
    Then it calculate length of all the splines (also new one) and filter out
    ones that are too short.
    """

    def __init__(
        self,
        connect_seg_if_closer_then=1000,
        cylinder_radius=200,
        filter_short_segments=1000,
    ):
        self.connect_seg_if_closer_then = connect_seg_if_closer_then
        self.filter_short_segments = filter_short_segments

        self.marge_splines = FilterConnectedNearSegments(
            distance_th=connect_seg_if_closer_then, cylinder_radius=cylinder_radius
        )

    def __call__(self, segments: np.ndarray) -> np.ndarray:
        """
        Connect splines that have their end's in close distance and remove
        splines that are too short.

        Args:
            segments (np.ndarray): Array of points with ID label of shape [ID, X, Y, Z]

        Returns:
            np.ndarray: Filtered array of connected MTs
        """
        """Do iterative optimization split 150 degree connection / marge"""
        # Split 150 degree connections
        loop_ = True
        while loop_:
            loop_, segments = cut_150_degree(segments)

        # Connect segments with ends close to each other
        border = [np.min(segments[:, 3]), np.max(segments[:, 3])]
        border = (border[1] - border[0]) / 50

        if self.connect_seg_if_closer_then > 0:
            segments = self.marge_splines(point_cloud=segments, omit_border=border)
            segments = reorder_segments_id(segments)

        """Remove too short splines"""
        if self.filter_short_segments > 0:
            length = []
            for i in np.unique(segments[:, 0]):
                length.append(
                    total_length(segments[np.where(segments[:, 0] == int(i))[0], 1:])
                )

            length = [
                id_ for id_, i in enumerate(length) if i > self.filter_short_segments
            ]

            new_seg = []
            for i in length:
                new_seg.append(segments[np.where(segments[:, 0] == i), :])

            if len(new_seg) > 0:
                segments = np.hstack(new_seg)[0, :]
                segments = reorder_segments_id(segments)

        # Split 150 degree connections
        loop_ = True
        while loop_:
            loop_, segments = cut_150_degree(segments)

        return reorder_segments_id(segments)


class SpatialGraphCompare:
    """
    Compare two spatial graphs and output filtered-out array's of splines based
    on similarity.

    This class take as na input two arrays of shape [n, 3 or 4] for 2D or 3D
    point cloud. This arrays contain [ID x X x Y x Z] dimensions.

    The comparison is archived by calculating cdist for all splines from one spatial
    graph to all splines from second spatial graph. And for each spline it output
    probability of similarity and splines id's.

    The Probability is calculated as a ration of points (in threshold contact)
    to all points in spline.

    The selection threshold for the spline interaction is given between 0 and 1.
    """

    def __init__(self, distance_threshold: int, interaction_threshold: float):
        self.dist_th = distance_threshold
        self.inter_th = interaction_threshold

    def _compare_spatial_graphs(
        self, spatial_graph_1: np.ndarray, spatial_graph_2: np.ndarray
    ) -> list:
        """
        Wrapper to compare all MT's between two spatial graphs

        Args:
            spatial_graph_1 (np.ndarray): Spatial graph 1.
            spatial_graph_2 (np.ndarray): Spatial graph 2.

        Returns:
            list: List of MT from spatial graph 1 that match spatial graph 2.
        """
        match_sg1_sg2 = []

        for i in np.unique(spatial_graph_1[:, 0]):
            sg1_spline = spatial_graph_1[spatial_graph_1[:, 0] == i, :]
            iou = []

            for j in np.unique(spatial_graph_2[:, 0]):
                sg2_spline = spatial_graph_2[spatial_graph_2[:, 0] == j, :]
                iou.append(
                    compare_splines_probability(
                        sg1_spline[:, 1:], sg2_spline[:, 1:], self.dist_th
                    )
                )

            ids = [
                id for id, i in enumerate(iou) if np.sum(i) > 0 and i >= self.inter_th
            ]
            match_sg1_sg2.append([i, ids])

        return match_sg1_sg2

    def __call__(
        self, amira_sg: np.ndarray, tardis_sg: np.ndarray
    ) -> Tuple[list, list]:
        """
        Compute comparison of Amira and Tardis spatial graphs and output tuple of
        arrays with different selected MTs:
            - Label1: MT taken from the Tardis (matches Amira)
            - Label2: MT taken from the Amira (matches Tardis)
            - Label3: MT in Tardis without match
            - Label4: MT in Amira without match

        Args:
            amira_sg (np.ndarray): Spatial graph [ID, X, Y, Z] from Amira.
            tardis_sg (np.ndarray): Spatial graph [ID, X, Y, Z] from tardis_em.

        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: Tuple of all arrays
        """
        label = [
            "TardisFilterBasedOnAmira",
            "TardisNoise",
            "AmiraFilterBasedOnTardis",
            "AmiraNoise",
        ]

        """Amira splines scores"""
        amira_comp = self._compare_spatial_graphs(
            spatial_graph_1=amira_sg, spatial_graph_2=tardis_sg
        )

        """Compare Tardis with Amira"""
        tardis_comp = self._compare_spatial_graphs(
            spatial_graph_1=tardis_sg, spatial_graph_2=amira_sg
        )

        # Select all splines from Tardis that match Amira
        match = [x[0] for x in tardis_comp if x[1] != []]
        tardis_match = np.stack([x for x in tardis_sg if x[0] in match])

        noise = [x[0] for x in tardis_comp if x[1] == []]
        tardis_noise = np.stack([x for x in tardis_sg if x[0] in noise])

        # Select all splines from Amira that match Tardis
        match = [x[0] for x in amira_comp if x[1] != []]
        amira_match = np.stack([x for x in amira_sg if x[0] in match])

        noise = [x[0] for x in amira_comp if x[1] == []]
        amira_noise = np.stack([x for x in amira_sg if x[0] in noise])

        spatial_graphs = [
            g
            for g in (tardis_match, tardis_noise, amira_match, amira_noise)
            if g is not None
        ]
        label = [
            l
            for g, l in zip(
                (tardis_match, tardis_noise, amira_match, amira_noise), label
            )
            if g is not None
        ]

        return spatial_graphs, label


def compare_splines_probability(
    spline_1: np.ndarray, spline_2: np.ndarray, threshold=100
):
    """
    Compare two splines and calculate probability of how likely given two
    splines are the same line given array of points for same or similar splines
    with no matching coordinates of points.

    Calculates the probability of two splines being similar by comparing
    the distance between their points and taking the mean of the matching
    points below a threshold.

    Parameters:
        spline_1 (np.ndarray): The first spline to compare, represented
            as an array of points.
        spline_2 (np.ndarray): The second spline to compare, represented
            as an array of points.
        threshold (int): The maximum distance between points for them to be
            considered matching.

    Returns:
        float: The probability of the splines being similar, ranging from 0.0 to 1.0.
    """
    if len(spline_1) == 0 or len(spline_2) == 0:
        return 0.0

    # Calculating distance matrix between points of 2 splines
    dist_matrix = cdist(spline_1, spline_2)

    # Check how many points on spline1 match spline2
    m_s1 = [1 if x < threshold else 0 for x in np.min(dist_matrix, axis=1)]

    # If no matching points probability is 0
    if sum(m_s1) == 0:
        return 0.0

    # Calculating intersection using % of the matching point below a threshold
    probability = sum(m_s1) / len(spline_1)

    return probability


def smooth_spline(points: np.ndarray, s=0.5):
    """
    Spline smoothing given an 's' smoothness factor.

    Args:
        points (np.ndarray): Point array [(ID), X, Y, Z] with optional ID and Z
        dimension.
        s (float): Smoothness factor.

    Returns:
        Returns: Smooth spline
    """
    if points.shape[1] == 4:  # [ID, X, Y, Z]
        id_ = int(points[0, 0])
        points = points[:, 1:]
        norm_pc = pc_median_dist(points)
        points = points / norm_pc

        t_before = tortuosity(points)
        try:
            tck, u = splprep(points.T, s=s)
            spline = np.stack(splev(u, tck)).T
        except ValueError:
            spline = points

        spline = spline * norm_pc
        t_after = tortuosity(spline)
        ids = np.zeros((len(spline), 1))
        ids[:, 0] = id_

        # Sanity check if spline smoothing failed
        if t_after > t_before:
            return np.hstack((ids, points * norm_pc))
        return np.hstack((ids, spline))
    else:  # [X, Y, Z]
        tck, u = splprep(points.T)

        return np.stack(splev(u, tck)).T


def sort_segment(coord: np.ndarray) -> np.ndarray:
    """
    Sorting of the point cloud based on number of connections followed by
    searching of the closest point with cdist.

    Args:
        coord (np.ndarray): Coordinates for each unsorted point idx.

    Returns:
        np.ndarray: Array of point in line order.
    """
    if len(coord) < 2:
        return coord

    new_c = []
    for i in range(len(coord) - 1):
        if i == 0:
            id = np.where(
                [sum(i) for i in cdist(coord, coord)]
                == max([sum(i) for i in cdist(coord, coord)])
            )[0]

            new_c.append(coord[id[0]])
            coord = np.delete(coord, id[0], 0)

        kd = KDTree(coord)
        points = kd.query(np.expand_dims(new_c[len(new_c) - 1], 0))[1][0][0]

        new_c.append(coord[points])
        coord = np.delete(coord, points, 0)

    if len(new_c) > 0:
        return np.stack(new_c)
    else:
        return coord


def reorder_segments_id(
    coord: np.ndarray,
    order_range: Optional[list] = None,
    order_list: Optional[Union[list, np.ndarray]] = None,
) -> np.ndarray:
    """
    Reorder list of segments to remove missing IDs

    E.g. Change IDs from [1, 2, 3, 5, 6, 8] to [1, 2, 3, 4, 5, 6]

    Args:
        coord: Array of points in 3D or 3D with their segment ID
        order_range: Costume id range for reordering
        order_list: List of reorder IDs to match to coord.

    Returns:
        np.ndarray: Array of points with reordered IDs values
    """
    df = np.unique(coord[:, 0])

    if order_range is None:
        df_range = np.asarray(range(0, len(df)), dtype=df.dtype)
    else:
        df_range = np.asarray(range(order_range[0], order_range[1]), dtype=df.dtype)

    if order_list is None:
        for id, i in enumerate(coord[:, 0]):
            coord[id, 0] = df_range[np.where(df == i)[0][0]]
    else:
        ordered_coord = []
        for i, new_id in zip(df, order_list):
            line = coord[np.where(coord[:, 0] == i)[0], :]
            line[:, 0] = new_id
            ordered_coord.append(line)
        coord = np.concatenate(ordered_coord)
        coord = reorder_segments_id(coord)

    return coord


def tortuosity(coord: np.ndarray) -> float:
    """
    Calculate spline tortuosity.

    Args:
        coord (np.ndarray): Coordinates for each unsorted point idx.

    Returns:
        float: Spline curvature measured with tortuosity.
    """
    if len(coord) <= 1:
        return 1.0

    length = total_length(coord) + 1e-16
    end_length = np.sqrt(np.sum((coord[0] - coord[-1]) ** 2) + 1e-16)

    return length / end_length


def total_length(coord: np.ndarray) -> float:
    """
    Calculate total length of the spline.

    Args:
        coord (np.ndarray): Coordinates for each unsorted point idx.

    Returns:
        float: Spline length.
    """
    length = 0
    c_len = len(coord) - 1

    for id, _ in enumerate(coord):
        if id == c_len:
            break

        # sqrt((x2 - x1)2 + (y2 - y1)2 + (z2 - z1)2)
        length += np.sqrt(np.sum((coord[id] - coord[id + 1]) ** 2))

    return length


def length_list(coord: np.ndarray) -> list:
    """
    Calculate total length of all splines and return it as a list.

    Args:
        coord (np.ndarray): Coordinates for each unsorted point idx.

    Returns:
        list: Spline length list.
    """
    spline_length_list = []

    for i in np.unique(coord[:, 0]):
        points = coord[np.where(coord[:, 0] == i)[0], 1:]
        spline_length_list.append(total_length(points))

    return spline_length_list


def angle_between_vectors(v1, v2):
    """
    Calculate the angle in degrees between two vectors.

    This function uses the dot product and the magnitudes of the vectors
    to calculate the angle between them according to the formula:

        cos(theta) = (A . B) / (||A|| ||B||)

    Args:
        v1(np.ndarray): First input vector.
        v2(np.ndarray): Second input vector.

    Returns:
        float The angle in degrees between vector 'v1' and 'v2'.
    """
    # Calculate the dot product of vectors v1 and v2
    dot_product = np.dot(v1, v2)

    # Calculate the magnitude (norm) of vectors
    magnitude_v1 = np.linalg.norm(v1) + 1e-16
    magnitude_v2 = np.linalg.norm(v2) + 1e-16

    # Calculate angle
    cos_theta = dot_product / (magnitude_v1 * magnitude_v2)
    angle = np.arccos(np.clip(cos_theta, -1.0, 1.0))

    return np.degrees(angle)


def cut_150_degree(segments_array: np.ndarray):
    """
    Cut segments based on angles between adjacent vectors.

    Given an array of line segments, this function calculates angles between
    adjacent vectors in each line. If the angle is less than or equal to 150
    degrees, the segment is cut into two new segments.

    Args:
    segments_array(np. ndarray): Array of line segments where the first column
    indicates the segment id and the remaining columns represent
    the coordinates of points.

    Args:
        segments_array:

    Returns:
        Tuple[bool, np.ndarray]: Indicates whether any segment was cut,
            and New array of cut segments.
    """

    cut_segments = []
    loop_ = False

    # Loop through unique segment IDs
    for i in np.unique(segments_array[:, 0]):
        pc_ = segments_array[np.where(segments_array[:, 0] == i)[0], 1:]

        angles_ = [180]

        # Calculate angles for each line segment
        for j in range(len(pc_) - 2):
            angles_.append(
                angle_between_vectors(
                    np.array(pc_[j]) - np.array(pc_[j + 1]),
                    np.array(pc_[j + 2]) - np.array(pc_[j + 1]),
                )
            )
        angles_.append(180)

        # Check if any angle is less than or equal to 150 degrees
        if len([id_ for id_, k in enumerate(angles_) if k <= 150]) > 0:
            loop_ = True

            # Find the minimum angle and cut the segment
            min_angle_idx = np.where(angles_ == np.min(angles_))[0][0]
            cut_segments.append(pc_[: min_angle_idx + 1, :])
            cut_segments.append(pc_[min_angle_idx + 1 :, :])
        else:
            cut_segments.append(pc_)

    # Filter out single-point segments
    cut_segments = [c for c in cut_segments if len(c) > 1]

    # Create the output array
    return loop_, np.vstack(
        [
            np.hstack((np.repeat(id_, len(c)).reshape(-1, 1), c))
            for id_, c in enumerate(cut_segments)
        ]
    )


def sort_by_length(coord):
    """
    Sort all splines by their length.

    Args:
        coord: Array of coordinates.

    Returns:
        np.ndarray: sorted and reorder splines.
    """
    length_list = []
    for i in np.unique(coord[:, 0]):
        length_list.append(total_length(coord[np.where(coord[:, 0] == i)[0], 1:]))

    sorted_id = np.argsort(length_list)

    sorted_list = [coord[np.where(coord[:, 0] == i)[0], 1:] for i in sorted_id]
    sorted_list = [
        np.hstack((np.repeat(i, len(sorted_list[i])).reshape(-1, 1), sorted_list[i]))
        for i in range(len(sorted_list))
    ]

    return np.concatenate(sorted_list)


class ComputeConfidenceScore:
    @staticmethod
    def _angle_smoothness(tangents):
        """
        Calculate the smoothness of a sequence of vectors based on the angles
        between consecutive vectors.

        The smoothness is computed as 1 minus the standard deviation of the angles between
        consecutive vectors. The angles are calculated using the dot product and
        magnitude of the vectors. A higher smoothness value indicates a more
        consistent alignment between consecutive vectors, whereas a lower smoothness value
        indicates more variability in the alignment.

        Args:
            tangents (np.ndarray): A 2D numpy array of shape (n, m), where n is
            the number of vectors and m is the dimension of each vector.
            Each row in the array represents a vector.

        Returns:
            float: A scalar value representing the smoothness of the sequence of vectors.
                Ranges from 0 to 1, with higher values indicating a smoother sequence.
        """
        if (
            not isinstance(tangents, np.ndarray)
            or tangents.ndim != 2
            or tangents.shape[0] < 2
        ):
            return 1.0
        else:
            magnitudes = np.linalg.norm(tangents, axis=1)
            non_zero_vectors = tangents[magnitudes > 0]

            # All vectors are approximately zero or there's only one non-zero vector
            if non_zero_vectors.shape[0] < 2:
                return 1.0

            angles = np.arccos(
                np.einsum("ij,ij->i", tangents[:-1], tangents[1:])
                / (
                    np.linalg.norm(tangents[:-1], axis=1)
                    * np.linalg.norm(tangents[1:], axis=1)
                )
            )
            smoothness = 1 - np.std(angles)
            return smoothness

    @staticmethod
    def normalized_length(points: np.ndarray, min_l: float, max_l: float):
        """
        Calculate and normalize the total length of a sequence of points.
        The total length is calculated using the `total_length` function.
        The result is then normalized to a value between 0 and 1 based on the provided
        minimum and maximum length values.

        Args:
            points (np.ndarray):
            min_l (float): The minimum length value.
            max_l (float): The maximum length value.
        """
        length = total_length(points)
        return (length - min_l) / (max_l - min_l + 1e-16)

    def combined_smoothness(self, points: np.ndarray, min_l: float, max_l: float):
        tangents = np.diff(points, axis=0)

        scores = [
            self._angle_smoothness(tangents),
            self.normalized_length(points, min_l, max_l),
        ]

        return np.mean(scores)

    def __call__(self, segments: np.ndarray):
        if segments.shape[1] != 4:
            TardisError(
                "145",
                "tardis_em.utils.spline_metric.py",
                f"Not segmented array. Expected shape 4 got {segments.shape[1]}",
            )
        unique_ids = np.unique(segments[:, 0])
        min_l = total_length(segments[np.where(segments[:, 0] == 0)[0], 1:])
        max_l = total_length(
            segments[np.where(segments[:, 0] == segments[-1, 0])[0], 1:]
        )

        scores = []
        for i in unique_ids:
            points = segments[np.where(segments[:, 0] == i)[0], 1:]
            scores.append(self.combined_smoothness(points, min_l, max_l))

        return scores
