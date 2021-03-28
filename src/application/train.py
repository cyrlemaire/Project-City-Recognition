
import os
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")

from src.infrastructure.model import make_image_scaler, make_data_augmenter, make_specific_learner, base_model
from src.infrastructure.data_loading import train_data, validation_data
from src.config.config import *


if __name__ == '__main__':

    # MAKE MODEL

    image_scaler = make_image_scaler()
    data_augmenter = make_data_augmenter()
    base_model.trainable = False
    specific_learner = make_specific_learner(len(CLASSES))

    inputs = tf.keras.Input(shape=IMAGE_SHAPE)
    x = image_scaler(inputs)
    x = data_augmenter(x)
    x = base_model(x, training=False)
    outputs = specific_learner(x)
    model = tf.keras.Model(inputs, outputs)

    # TRAIN MODEL
    print('===========')
    print('TRAIN MODEL')
    print('===========')

    model.compile(
        optimizer=tf.keras.optimizers.Adam(),
        loss='categorical_crossentropy',
        metrics='accuracy',
    )

    model.fit(train_data, validation_data=validation_data, epochs=EPOCHS)

    # OPTIONALLY RETRAIN

    if RETRAIN:
        base_model.trainable = True
        model.compile(
            optimizer=tf.keras.optimizers.Adam(1e-5),
            loss='categorical_crossentropy',
            metrics=['accuracy'],
        )

        model.fit(train_data, validation_data=validation_data, epochs=EPOCHS_RETRAIN)

    print('==========')
    print('SAVE MODEL')
    print('==========')

    model.save(filepath=os.path.join(MODEL_DIR, 'PCR_model'))
