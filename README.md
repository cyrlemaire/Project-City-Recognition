# Project City Recognition

This is Yotta’s project #2 by Olivier Collier, Cyril Lemaire and Julien Sadoun. We designed an application that can recognize the city in which a given picture has been taken. Our algorithm analyses architecture, colors and patterns to make a prediction.

We proposed a solution based on transfer learning, building on DenseNet201. It creates a proof of concept, that takes only five cities into account: Amsterdam, London, Paris, Strasbourg and Venice.

# Prerequisites

Our project requires the following tools:


* Python 3.8, see download page [here](https://www.python.org/downloads/),


* wget, see download page [here](https://www.gnu.org/software/wget/),


* Poetry, see download page [here](https://python-poetry.org/docs/).

# Getting started


1. **Clone this repository**

```
git clone <this project>
cd <this project>
```


1. **Set up virtual environment**

Set up a Poetry environment by running the following command:

```
poetry install
poetry shell
```

If you have several versions of Python on your computer, you may need to run the following command prior to installing Poetry:

```
poetry env use /full/path/to/python3.8
```


1. **Download image dataset**

To download the necessary image dataset for training and testing, run the following commands from the repository root:

```
wget “https://www.dropbox.com/sh/1ks98px6egwjp31/AAAZh1LuvQzs5-9Cu9u2dQHka?dl=0” --content-disposition
unzip data.zip && rm data.zip
```


1. **Train the model**

To train a model using the previously downloaded dataset, run the following command from the repository root:

```
poetry shell
poetry run python src/application/train.py
```


1. **Make predictions from the model**

To test our final model (not the one trained above, but the one we selected), run the following command from the repository root:

```
poetry shell
poetry run python src/application/predict.py
```


1. **Test our web-app!**

To access our web-app and interactively use your own pictures, run the following command from the repository root:

```
poetry shell
streamlit run src/application/application.py
```

# Indices and tables


* Index


* Module Index


* Search Page
