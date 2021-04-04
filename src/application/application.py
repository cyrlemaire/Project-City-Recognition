import cv2
import numpy as np
import os
import pandas as pd
import src.config.config as config
import streamlit as st
import tensorflow as tf


from keras.preprocessing.image import img_to_array
from PIL import Image, ImageOps


"""
# Projet n°2 - Project City Recognition
"""

model = tf.keras.models.load_model(os.path.join(config.MODEL_DIR, 'PCR_model.hdf5'))
st.write("Bienvenue dans notre modèle de prédiction de ville à partir d'une photo ! Le principe est simple : insérez une photo de façade de bâtiment, et le modèle essaiera de deviner la ville dont la photo provient (Parmi les villes de Paris, Amsterdam, Strasbourg, Londres et Venise) !")
image_data = st.file_uploader("Veuillez insérer une image afin de commencer la prédiction :", type=["jpg", "png"])


def import_and_predict(image_data, model):
    """Imports the image and predict the outcome based on the pre-trained model."""
    size = (150, 150)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    image = np.asarray(image)
    img_resize = (cv2.resize(image, dsize=(150, 150), interpolation=cv2.INTER_CUBIC))
    img_reshape = img_resize[np.newaxis, ...]
    prediction = model.predict(img_reshape)
    return prediction


if image_data is not None:
    image = Image.open(image_data)
    st.image(image, caption='Image à classifier', use_column_width=True)
    prediction = import_and_predict(image, model)

    if np.argmax(prediction) == 0:
        st.write("La ville prédite par le modèle est Amsterdam ! 🇳🇱 🌷")
        map_data = pd.DataFrame(
            np.random.randn(1, 1) / [500, 500] + [52.3738, 4.89093],
            columns=['lat', 'lon'])
        st.map(map_data, zoom=8)
    elif np.argmax(prediction) == 1:
        st.write("La ville prédite par le modèle est Londres ! 🇬🇧 👑")
        map_data = pd.DataFrame(
            np.random.randn(1, 1) / [500, 500] + [51.5072, -0.1275],
            columns=['lat', 'lon'])
        st.map(map_data, zoom=8)
    elif np.argmax(prediction) == 2:
        st.write("La ville prédite par le modèle est Paris ! 🇫🇷 🗼")
        map_data = pd.DataFrame(
            np.random.randn(1, 1) / [500, 500] + [48.856614, 2.3522219],
            columns=['lat', 'lon'])
        st.map(map_data, zoom=8)
    elif np.argmax(prediction) == 3:
        st.write("La ville prédite par le modèle est Strasbourg ! 🇫🇷 🥨")
        map_data = pd.DataFrame(
            np.random.randn(1, 1) / [500, 500] + [48.5734053, 7.7521113],
            columns=['lat', 'lon'])
        st.map(map_data, zoom=8)
    elif np.argmax(prediction) == 4:
        st.write("La ville prédite par le modèle est Venise ! 🇮🇹 🎭")
        map_data = pd.DataFrame(
            np.random.randn(1, 1) / [500, 500] + [45.4408474, 12.3155151],
            columns=['lat', 'lon'])
        st.map(map_data, zoom=8)
    else:
        raise ValueError
