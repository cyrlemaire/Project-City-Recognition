
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")

import src.config.config as config


def train_validation_data_generator():
    """Loads generators for train and validation data."""
    dataflow_kwargs = dict(target_size=config.IMAGE_SIZE,
                           batch_size=config.BATCH_SIZE,
                           interpolation=config.INTERPOLATION)
    train_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=12,
                                                                           horizontal_flip=True,
                                                                           width_shift_range=0.1,
                                                                           height_shift_range=0.1,
                                                                           shear_range=0.2,
                                                                           zoom_range=0.3,
                                                                           channel_shift_range=20,
                                                                           validation_split=config.VALIDATION_SPLIT)
    train_generator = train_data_generator.flow_from_directory(config.TRAIN_DATA_DIR,
                                                               subset="training",
                                                               shuffle=True,
                                                               **dataflow_kwargs)
    validation_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(validation_split=config.VALIDATION_SPLIT)
    validation_generator = validation_data_generator.flow_from_directory(config.TRAIN_DATA_DIR,
                                                                         subset="validation",
                                                                         shuffle=False,
                                                                         **dataflow_kwargs)
    return train_generator, validation_generator


def load_test_data():
    """Loads test data."""
    test_data = tf.keras.preprocessing.image_dataset_from_directory(
        config.TEST_DATA_DIR,
        labels="inferred",
        label_mode="categorical",
        class_names=config.CLASSES,
        batch_size=config.BATCH_SIZE,
        shuffle=False,
        image_size=config.IMAGE_SIZE,
        validation_split=None
    )

    return test_data

