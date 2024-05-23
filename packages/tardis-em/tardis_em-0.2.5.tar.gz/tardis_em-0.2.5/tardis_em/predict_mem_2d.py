#######################################################################
#  TARDIS - Transformer And Rapid Dimensionless Instance Segmentation #
#                                                                     #
#  New York Structural Biology Center                                 #
#  Simons Machine Learning Center                                     #
#                                                                     #
#  Robert Kiewisz, Tristan Bepler                                     #
#  MIT License 2021 - 2024                                            #
#######################################################################

import warnings
from os import getcwd

import click

from tardis_em.utils.predictor import GeneralPredictor
from tardis_em._version import version
from tardis_em.utils.errors import TardisError
from tardis_em import format_choices

# from tardis_em.utils.ota_update import ota_update
# ota = ota_update()
warnings.simplefilter("ignore", UserWarning)


@click.command()
@click.option(
    "-dir",
    "--path",
    default=getcwd(),
    type=str,
    help="Directory with images for prediction with CNN model.",
    show_default=True,
)
@click.option(
    "-ms",
    "--mask",
    default=False,
    type=bool,
    help="Define if your input is a binary mask with pre-segmented membrane.",
    show_default=True,
)
@click.option(
    "-px",
    "--correct_px",
    default=None,
    type=float,
    help="Correct pixel size values.",
    show_default=True,
)
@click.option(
    "-ch",
    "--checkpoint",
    default="None|None",
    type=str,
    help="Optional list of pre-trained weights",
    show_default=True,
)
@click.option(
    "-cnn",
    "--convolution_nn",
    default="fnet_attn",
    type=str,
    help="Select CNN used for semantic segmentation.",
    show_default=True,
)
@click.option(
    "-out",
    "--output_format",
    default="mrc_csv",
    type=click.Choice(format_choices),
    help="Type of output files. The First optional output file is the binary mask "
    "which can be of type None [no output], am [Amira], mrc or tif. "
    "Second output is instance segmentation of objects, which can be "
    "output as amSG [Amira], mrcM [mrc mask], tifM [tif mask], "
    "csv coordinate file [ID, X, Y] or None [no instance prediction].",
    show_default=True,
)
@click.option(
    "-ps",
    "--patch_size",
    default=256,
    type=int,
    help="Size of image patch used for prediction. This will break "
    "the tomogram volumes into 3D patches where each patch will be "
    "separately predicted and then stitched back together "
    "with 25% overlap.",
    show_default=True,
)
@click.option(
    "-rt",
    "--rotate",
    default=True,
    type=bool,
    help="If True, during CNN prediction image is rotate 4x by 90 degrees."
    "This will increase prediction time 4x. However may lead to more cleaner"
    "output.",
    show_default=True,
)
@click.option(
    "-ct",
    "--cnn_threshold",
    default=0.25,
    type=float,
    help="Threshold used for CNN prediction.",
    show_default=True,
)
@click.option(
    "-dt",
    "--dist_threshold",
    default=0.5,
    type=float,
    help="Threshold used for instance prediction.",
    show_default=True,
)
@click.option(
    "-pv",
    "--points_in_patch",
    default=900,
    type=int,
    help="Size of the cropped point cloud, given as a max. number of points "
    "per crop. This will break generated from the binary mask "
    "point cloud into smaller patches with overlap.",
    show_default=True,
)
@click.option(
    "-cc",
    "--connect_cylinder",
    default=40,
    type=int,
    help="To minimize false positives when linking membranes, we limit "
    "the search area to a cylindrical radius specified in angstroms. "
    "For each spline, we find the direction the filament end is pointing in "
    "and look for another filament that is oriented in the same direction. "
    "The ends of these filaments must be located within this cylinder "
    "to be considered connected.",
    show_default=True,
)
@click.option(
    "-cm",
    "--connect_membranes",
    default=1000,
    type=int,
    help="To address the issue where membrane are mistakenly "
    "identified as two different filaments, we use a filtering technique. "
    "This involves identifying the direction each membranes end points and then "
    "linking any membranes that are facing the same direction and are within "
    "a certain distance from each other, measured in angstroms. This distance threshold "
    "determines how far apart two membranes can be, while still being considered "
    "as a single unit if they are oriented in the same direction.",
    show_default=True,
)
@click.option(
    "-dv",
    "--device",
    default=0,
    type=str,
    help="Define which device to use for training: "
    "gpu: Use ID 0 GPU"
    "cpu: Usa CPU"
    "mps: Apple silicon"
    "0-9 - specified GPU device id to use",
    show_default=True,
)
@click.option(
    "-db",
    "--debug",
    default=False,
    type=bool,
    help=" If True, save the output from each step for debugging.",
    show_default=True,
)
@click.version_option(version=version)
def main(
    path: str,
    mask: bool,
    correct_px: float,
    convolution_nn: str,
    checkpoint: str,
    output_format: str,
    patch_size: int,
    rotate: bool,
    cnn_threshold: float,
    dist_threshold: float,
    points_in_patch: int,
    connect_splines: int,
    connect_membranes: int,
    device: str,
    debug: bool,
):
    """
    MAIN MODULE FOR PREDICTION MT WITH TARDIS-PYTORCH
    """
    if output_format.split("_")[1] == "None":
        instances = False
    else:
        instances = True

    checkpoint = checkpoint.split("|")
    if len(checkpoint) != 2:
        TardisError(
            id_="00",
            py="tardis_em/predict_mt.py",
            desc="Two checkpoint are expected!",
        )
    elif len(checkpoint) == 2:
        if checkpoint[0] == "None":
            checkpoint[0] = None
        if checkpoint[1] == "None":
            checkpoint[1] = None

    predictor = GeneralPredictor(
        predict="Membrane2D",
        dir_=path,
        binary_mask=mask,
        correct_px=correct_px,
        convolution_nn=convolution_nn,
        checkpoint=checkpoint,
        output_format=output_format,
        patch_size=patch_size,
        cnn_threshold=cnn_threshold,
        dist_threshold=dist_threshold,
        points_in_patch=points_in_patch,
        predict_with_rotation=rotate,
        instances=instances,
        connect_splines=connect_splines,
        connect_cylinder=connect_membranes,
        device_=str(device),
        debug=debug,
    )
    predictor()


if __name__ == "__main__":
    main()
