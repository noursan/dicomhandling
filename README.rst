dicomhandling
=============

.. image:: https://github.com/noursan/dicomhandling/blob/master/data/input/T1_3D_TFE%20-%20301/residues/unfiltered_residue.jpg?raw=true
  :width: 200
  :alt: Unfiltered residue
.. image:: https://github.com/noursan/dicomhandling/blob/master/data/input/T1_3D_TFE%20-%20301/residues/filtered_residue.jpg?raw=true
  :width: 200
  :alt: Filtered residue

``dicomhandling`` is a python module to showcase some basic DICOM image manipulation.

Installation
------------

These instructions will get you a copy of the project up and running on your local machine.

Open a terminal window and clone this repository by writing:

.. code-block:: bash

    git clone https://github.com/noursan/dicomhandling

To use ``dicomhandling`` several `Python 3 <https://www.python.org/>`__ packages are required. Creating a brand new `Conda <https://docs.conda.io/en/latest/>`__ environment for this is recommended. This can be done easily with the provided ``environment.yml`` file as follows:

.. code-block:: bash

    conda env create -f environment.yml
    conda activate quibim

The environment is self-contained to not influence other local python installations and avoid conflicts with previously installed packages. 

To deactivate the ``quibim`` environment simply type:

.. code-block:: bash

    conda deactivate

Usage
-----

You can check out the usage of the module by executing it by:

.. code-block:: bash

    python -m dicomhandling './data/input/T1_3D_TFE - 301'

This will generate the filtered and unfiltered residues in a folder inside the input path.

You can also access the functions coded in the ``dicomhandling`` module by importing the module from your own python script:

.. code-block:: python

    import dicomhandling as dh

Authors
-------

-  `Nour Sánchez <https://github.com/noursan>`__
