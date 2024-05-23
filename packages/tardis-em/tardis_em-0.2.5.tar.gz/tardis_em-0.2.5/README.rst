.. image:: resources/Tardis_logo_2.png
    :width: 512
    :align: center
    :target: https://smlc-nysbc.github.io/TARDIS/

========

.. image:: https://github.com/SMLC-NYSBC/TARDIS/actions/workflows/python_pytest.yml/badge.svg
        :target: https://github.com/SMLC-NYSBC/TARDIS/actions/workflows/python_pytest.yml

.. image:: https://github.com/SMLC-NYSBC/TARDIS/actions/workflows/licensed.yml/badge.svg
        :target: https://github.com/SMLC-NYSBC/TARDIS/actions/workflows/licensed.yml

.. image:: https://github.com/SMLC-NYSBC/TARDIS/actions/workflows/sphinx_documentation.yml/badge.svg
        :target: https://github.com/SMLC-NYSBC/TARDIS/actions/workflows/sphinx_documentation.yml

.. image:: https://img.shields.io/badge/Join%20Our%20Community-Slack-blue
        :target: https://join.slack.com/t/tardis-em/shared_invite/zt-27jznfn9j-OplbV70KdKjkHsz5FcQQGg


Python-based software for generalized object instance segmentation from (cryo-)electron microscopy
micrographs/tomograms. The software package is built on a general workflow where predicted semantic segmentation
is used for instance segmentation of 2D/3D images.

.. image:: resources/workflow.png

Features
========

- Robust and high-throughput semantic/instance segmentation of all microtubules:
    - Supported file formats: [.tif, .mrc, .rec, .am]
    - Supported modality: [ET, Cryo-ET]
    - Supported Å resolution: [any best results in 1-40 Å range]
    - 2D micrograph modality microtubule segmentation will come soon!

- Robust and high-throughput semantic/instance segmentation of membranes:
    - Supported file formats: [.tif, .mrc, .rec, .am]
    - Supported modality: [EM, ET, Cryo-EM, Cryo-ET]
    - Supported Å resolution: [all]

- High-throughput semantic/instance segmentation of actin [Beta]
- Fully automatic segmentation solution!
- Napari plugin [Coming soon]
- Cloud computing [Coming soon]

Citation
========

`DOI [Microscopy and Microanalysis] <http://dx.doi.org/10.1093/micmic/ozad067.485>`__

Kiewisz R., Fabig G., Müller-Reichert T. Bepler T. 2023. Automated Segmentation of 3D Cytoskeletal Filaments from Electron Micrographs with TARDIS. Microscopy and Microanalysis 29(Supplement_1):970-972.

`Link: NeurIPS 2022 MLSB Workshop <https://www.mlsb.io/papers_2022/Membrane_and_microtubule_rapid_instance_segmentation_with_dimensionless_instance_segmentation_by_learning_graph_representations_of_point_clouds.pdf>`__

Kiewisz R., Bepler T. 2022. Membrane and microtubule rapid instance segmentation with dimensionless instance segmentation by learning graph representations of point clouds. Neurips 2022 - Machine Learning for Structural Biology Workshop.

What's new?
===========

`Full History <https://smlc-nysbc.github.io/TARDIS/HISTORY.html>`__

TARDIS-em v0.2.5 (2024-05-22):
    * Added actin segmentation
    * Improvement from Microtubule and Membrane prediction with updated models
    * Added option for scripting TARDIS predictions
    * Added visualization for semantic and instance predictions
    * TARDIS build in results visualization
    * Bug fixes
    * Documentation tutorials
    * Pypi and Conda releases
    * Re-trained DIST model using simulated datasets
    * Build 2 model for:
        * filaments and general 2D structures
        * 3D objects like membranes mitochondria LiDAR data etc.

Quick Start
===========

For more examples and advanced usage please find more details in our `Documentation <https://smlc-nysbc.github.io/TARDIS/>`__

1) Install TARDIS-em:

.. code-block:: bash

    pip install tardis-em

or

.. code-block:: bash

    conda install tardis-em -c rrobert92

2) Verifies installation:

.. code-block:: bash

    tardis

Filaments Prediction
--------------------

3D Actin prediction
^^^^^^^^^^^^^^^^^^^
Full tutorial: `3D Actin Prediction <https://smlc-nysbc.github.io/TARDIS/usage/3d_actin.html>`__

Usage:
""""""

.. code-block:: bash

    recommended usage: tardis_actin [-dir path/to/folder/with/input/tomogram]
    advance usage: tardis_actin [-dir str] [-out str] [-ps int] [-ct float] [-dt float]
                             [-pv int] [-px float] ...


2D Microtubule prediction
^^^^^^^^^^^^^^^^^^^^^^^^^

TBD

3D Microtubule prediction
^^^^^^^^^^^^^^^^^^^^^^^^^
Full tutorial: `3D Microtubules Prediction <https://smlc-nysbc.github.io/TARDIS/usage/3d_mt.html>`__


Example:
""""""""

.. image:: resources/3d_mt.jpg

Data source: Dr. Gunar Fabig and Prof. Dr. Thomas Müller-Reichert, TU Dresden


Usage:
""""""

.. code-block:: bash

    recommended usage: tardis_mt [-dir path/to/folder/with/input/tomogram]
    advance usage: tardis_mt [-dir str] [-out str] [-ps int] [-ct float] [-dt float]
                             [-pv int] [-px float] ...


Membrane Prediction
-------------------

2D prediction
^^^^^^^^^^^^^
Full tutorial: `2D Membrane Prediction <https://smlc-nysbc.github.io/TARDIS/usage/2d_membrane.html>`__

Example:
""""""""

.. image:: resources/2d_mem.jpg

Data source: Dr. Victor Kostyuchenko and Prof. Dr. Shee-Mei Lok, DUKE-NUS Medical School Singapore

Usage:
""""""

.. code-block:: bash

    recommended usage: tardis_mem2d [-dir path/to/folder/with/input/tomogram] -out mrc_csv
    advance usage: tardis_mem [-dir str] [-out str] [-ps int] ...

3D prediction
^^^^^^^^^^^^^
Full tutorial: `3D Membrane Prediction <https://smlc-nysbc.github.io/TARDIS/usage/3d_membrane.html>`__

Example:
""""""""

.. image:: resources/3d_mem.jpg

Data source: EMPIRE-10236, DOI: 10.1038/s41586-019-1089-3

Usage:
""""""

.. code-block:: bash


    recommended usage: tardis_mem [-dir path/to/folder/with/input/tomogram] -out mrc_csv
    advance usage: tardis_mem [-dir str] [-out str] [-ps int] ...
