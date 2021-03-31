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

    # set up a schedule for learning rate decay
    lr_schedule = tf.keras.optimizers.schedules.PolynomialDecay(
        initial_learning_rate=INITIAL_LEARNING_RATE,
        end_learning_rate=FINAL_LEARNING_RATE,
        decay_steps=DECAY_STEPS,
        power=1.0,
        cycle=False,
        name=None
    )

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=lr_schedule),
        loss='categorical_crossentropy',
        metrics='accuracy',
    )

    model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=CHECKPOINT_FILE_PATH,
        monitor='val_accuracy',
        mode='max',
        verbose=1,
        save_best_only=True)

    model.fit(train_generator,
              validation_data=valid_generator,
              epochs=EPOCHS,
              callbacks=[model_checkpoint_callback])

    # OPTIONALLY RETRAIN

    if RETRAIN:
        base_model.trainable = True
        model.compile(
            optimizer=tf.keras.optimizers.Adam(1e-5),
            loss='categorical_crossentropy',
            metrics=['accuracy'],
        )

        model.fit(train_generator,
                  validation_data=valid_generator,
                  epochs=EPOCHS_RETRAIN,
                  callbacks=[model_checkpoint_callback])

    print('==========')
    print('SAVE MODEL')
    print('==========')

    model.save(filepath=os.path.join(MODEL_DIR, MODEL_NAME))
