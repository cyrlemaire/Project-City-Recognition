
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")

from src.config.config import *


def load_train_data():

    train_data = tf.keras.preprocessing.image_dataset_from_directory(
        TRAIN_DATA_DIR,
        labels="inferred",
        label_mode="categorical",
        class_names=CLASSES,
        batch_size=BATCH_SIZE,
        image_size=IMAGE_SIZE,
        shuffle=True,
        seed=SEED,
        validation_split=VALIDATION_SPLIT,
        subset='training'
    )

    validation_data = tf.keras.preprocessing.image_dataset_from_directory(
        TRAIN_DATA_DIR,
        labels="inferred",
        label_mode="categorical",
        class_names=CLASSES,
        batch_size=BATCH_SIZE,
        image_size=IMAGE_SIZE,
        shuffle=True,
        seed=SEED,
        validation_split=VALIDATION_SPLIT,
        subset='validation'
    )

    return train_data, validation_data


def load_test_data():

    test_data = tf.keras.preprocessing.image_dataset_from_directory(
        TEST_DATA_DIR,
        labels="inferred",
        label_mode="categorical",
        class_names=CLASSES,
        batch_size=BATCH_SIZE,
        shuffle=False,
        image_size=IMAGE_SIZE,
        validation_split=None
    )

    return test_data
