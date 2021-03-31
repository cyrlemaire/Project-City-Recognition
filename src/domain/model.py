
import tensorflow as tf
from tensorflow.keras import Model
import warnings
warnings.filterwarnings("ignore")

from src.config.config import *


def make_image_scaler():
    image_rescaler = tf.keras.Sequential([
      tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
    ])
    return image_rescaler


def make_specific_learner(number_classes):
    specific_learner = tf.keras.Sequential([
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dropout(.3),
        tf.keras.layers.Dense(256),
        tf.keras.layers.Dropout(.3),
        tf.keras.layers.Dense(128),
        tf.keras.layers.Dropout(.3),
        tf.keras.layers.Dense(64),
        tf.keras.layers.Dense(number_classes, activation='softmax')
    ])
    return specific_learner


base_model = tf.keras.applications.Xception(
    weights="imagenet",
    input_shape=IMAGE_SHAPE,
    include_top=False,
)
