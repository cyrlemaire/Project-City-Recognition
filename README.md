# Project N°2 - Yotta Academy - Advanced ML : Project City Recognition 

Copyright : Olivier Collier, Cyril LEMAIRE & Julien SADOUN

## Context

As an assignment, we created a computer vision program able to identify the city of origin of a random building, based on its picture. The model created for this purpose is based on the DenseNet (Dense Convolutional Network) model, and works on 5 cities: London, Paris, Amsterdam, Venice and Strasbourg. An Stre

## Program interface

TODO => streamlit UI

## Main code

The following sections describe the source code of the project and explain how to use it to retrain the model on the city images dataset.

## Project Arborescence
TODO

## Pre-requisites

Tools needed to run the code :

- wget: Please find the documentatioin [at this address](https://www.gnu.org/software/wget/)
- Poetry : Please find the documentation [at this address](https://python-poetry.org/docs/)
- Python 3.8.5 : Please find the documentation [at this address](https://www.python.org/downloads/release/python-385/)

## Getting Started

### 1. Clone this repository
```
$ git clone <this project>
$ cd <this project>
```
### 2. Setup your environment

First, please install the required dependencies with [Poetry](https://python-poetry.org).
In the folder containing the poetry.toml, write in your terminal
```
$ poetry install
```
For this specific purpose, you can use the env use command to tell Poetry which Python version to use for the current project:

```
$ poetry env use /full/path/to/python
```
### 3. Download the dataset

To download the train pictures in the TRAIN_DATA_DIR directory, simply exectute this command:
````
$ TRAIN_DATA_DIR=<your train directory path>
$ cd $TRAIN_DATA_DIR
$ wget “https://www.dropbox.com/sh/1ks98px6egwjp31/AAAZh1LuvQzs5-9Cu9u2dQHka?dl=0” --content-disposition
$ unzip data_ProjectCityRecognition.zip
$ rm data_ProjectCityRecognition.zip
```
###4. Complete config.py file

TODO

### 5. Train the model

TODO

###6. Predict

TODO ?

