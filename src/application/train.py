import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")

from src.domain.model import make_image_scaler, make_specific_learner, base_model
from src.infrastructure.data_generator import train_generator, valid_generator
from src.config.config import *


if __name__ == '__main__':

    # MAKE MODEL

    image_scaler = make_image_scaler()
    base_model.trainable = False
    specific_learner = make_specific_learner(len(CLASSES))

    inputs = tf.keras.Input(shape=IMAGE_SHAPE)
    x = image_scaler(inputs)
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

    model.fit(train_generator, validation_data=valid_generator, epochs=EPOCHS)

    # OPTIONALLY RETRAIN

    if RETRAIN:
        base_model.trainable = True
        model.compile(
            optimizer=tf.keras.optimizers.Adam(1e-5),
            loss='categorical_crossentropy',
            metrics=['accuracy'],
        )

        model.fit(train_generator, validation_data=valid_generator, epochs=EPOCHS_RETRAIN)

    print('==========')
    print('SAVE MODEL')
    print('==========')

    model.save(filepath=os.path.join(MODEL_DIR, MODEL_NAME))
