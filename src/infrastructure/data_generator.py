import tensorflow as tf
import warnings

warnings.filterwarnings("ignore")

from src.config.config import *

# loading arguments for generators

dataflow_kwargs = dict(target_size=IMAGE_SIZE,
                       batch_size=BATCH_SIZE,
                       interpolation=INTERPOLATION
                       )

# Instanciate image data generator for validation
valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(validation_split=VALIDATION_SPLIT)

# Create validation dataset
valid_generator = valid_datagen.flow_from_directory(TRAIN_DATA_DIR,
                                                    subset="validation",
                                                    shuffle=False,
                                                    **dataflow_kwargs
                                                    )

if D0_DATA_AUGMENTATION:

    # Instanciate image data generator for train batchs with augmantation
    train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=12,
                                                                    horizontal_flip=True,
                                                                    width_shift_range=0.1,
                                                                    height_shift_range=0.1,
                                                                    shear_range=0.2,
                                                                    zoom_range=0.3,
                                                                    channel_shift_range=20,
                                                                    validation_split=VALIDATION_SPLIT
                                                                    )
else:

    # Instanciate image data generator for train batchs without augmentation
    train_datagen = valid_datagen

# generator for train dataset
train_generator = train_datagen.flow_from_directory(TRAIN_DATA_DIR,
                                                    subset="training",
                                                    shuffle=True,
                                                    **dataflow_kwargs
                                                    )


# Load data for test

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

