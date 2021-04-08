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


2. **Set up virtual environment**

Set up a Poetry environment by running the following command:

```
poetry install
poetry shell
```

If you have several versions of Python on your computer, you may need to run the following command prior to installing Poetry:

```
poetry env use /full/path/to/python3.8
```


3. **Download image dataset**

To download the necessary image dataset for training and testing, run the following commands from the repository root:

```
wget 'https://www.dropbox.com/sh/1ks98px6egwjp31/AAAZh1LuvQzs5-9Cu9u2dQHka?dl=0' --content-disposition
unzip data.zip
rm data.zip
```


4. **Train the model**

To train a model using the previously downloaded dataset, run the following command from the repository root:

```
poetry run python src/application/train.py
```


5. **Make predictions from the model**

To test our final model (not the one trained above, but the one we selected), run the following command from the repository root:

```
poetry run python src/application/predict.py
```


6. **Test our web-app!**

To access our web-app and interactively use your own pictures, run the following command from the repository root:

```
streamlit run src/application/application.py
```

7. **Image scrapping**

To create your own image dataset, you can use our script to scrap images on Google. First complete the src/config/scrap_config_template.py file with the folder in which you want to dowload images and the queries to use in Google Image. Then run the following command from the repository root:

```
poetry run python src/infrastructure/data_scraping.py
```

If you have duplicates in your folder you can run:

```
poetry run python src/infrastructure/remove_duplicates.py
```

to delete them.

8. **Documentation**

If you want to consult the project documentation, run the following command from the repository root:

```
open docs/build/html/index.html
```


# Repository architecture

```
├── README.md
├── data
│   ├── test
│   └── train
├── docs
│   ├── Makefile
│   ├── build
│   │   └── html
│   │       ├── genindex.html
│   │       ├── index.html
│   │       ├── modules.html
│   │       ├── objects.inv
│   │       ├── py-modindex.html
│   │       ├── search.html
│   │       ├── searchindex.js
│   │       ├── src.application.html
│   │       ├── src.config.html
│   │       ├── src.domain.html
│   │       ├── src.html
│   │       └── src.infrastructure.html
│   ├── commands.rst
│   ├── conf.py
│   ├── getting-started.rst
│   ├── index.rst
│   └── make.bat
├── models
│   └── PCR_model.hdf5
├── pyproject.toml
└── src
    ├── __init__.py
    ├── application
    │   ├── __init__.py
    │   ├── application.py
    │   ├── predict.py
    │   └── train.py
    ├── config
    │   ├── __init__.py
    │   └── config.py
    │   └── scrap_config_template.py
    ├── domain
    │   ├── __init__.py
    │   └── model.py
    └── infrastructure
        ├── __init__.py
        ├── data_generator.py
        ├── data_scraping.py
        └── remove_duplicates.py
```
