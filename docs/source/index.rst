
Project City Recognition
=========================

This is Yotta's project #2 by Olivier Collier, Cyril Lemaire and Julien Sadoun. We designed an application that can recognize the city in which a given picture has been taken. Our algorithm analyses architecture, colors and patterns to make a prediction.

We proposed a solution based on transfer learning, building on DenseNet201. It creates a proof of concept, that takes only five cities into account: Amsterdam, London, Paris, Strasbourg and Venice. 

Prerequisites
=============

Our project requires the following tools:

- Python 3.8, see download page `here <https://www.python.org/downloads/>`_,

- wget, see download page `here <https://www.gnu.org/software/wget/>`_,

- Poetry, see download page `here <https://python-poetry.org/docs/>`_.

Getting started
===============

1. **Clone this repository**  

.. code-block:: bash

    git clone <this project>
    cd <this project>

2. **Set up virtual environment**

Set up a Poetry environment by running the following command:

.. code-block:: bash

    poetry install
    poetry shell
	
If you have several versions of Python on your computer, you may need to run the following command prior to installing Poetry:

.. code-block:: bash

    poetry env use /full/path/to/python3.8

3. **Download image dataset**

To download the necessary image dataset for training and testing, run the following commands from the repository root:

.. code-block:: bash    

    wget “https://www.dropbox.com/sh/1ks98px6egwjp31/AAAZh1LuvQzs5-9Cu9u2dQHka?dl=0” --content-disposition
    unzip data.zip && rm data.zip

4. **Train the model**

To train our model using the previously downloaded dataset, run the following command from the repository root:

.. code-block:: bash

    poetry shell
    poetry run python src/application/train.py

5. **Make predictions from the model**

To test the 

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
