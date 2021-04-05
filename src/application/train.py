
import logging
import os
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")

import src.config.config as config
from src.domain.model import CustomModel
from src.infrastructure.data_generator import train_validation_data_generator

logging.basicConfig(format='%(message)s', level=logging.INFO)


class ModelTraining:

    def __init__(self, model):
        self.model = model
        self.tmp_path = os.path.join(config.MODEL_DIR, 'tmp.hdf5')

    def train(self, train_generator, validation_generator, epochs, kwd):
        """Trains model."""
        self._set_optimization_parameters(kwd)
        self.model.fit(train_generator,
                       validation_data=validation_generator,
                       epochs=epochs,
                       callbacks=[self.checkpoint])
        self._restore_best_model()

    def save(self, path):
        """Saves model to given path."""
        self.model.save_weights(filepath=path)

    @property
    def learning_rate_scheduler(self):
        """Custom learning rate scheduler."""
        lr_scheduler = tf.keras.optimizers.schedules.PolynomialDecay(
            initial_learning_rate=config.INITIAL_LEARNING_RATE,
            end_learning_rate=config.FINAL_LEARNING_RATE,
            decay_steps=config.DECAY_STEPS,
            power=1.0,
            cycle=False,
            name=None
        )
        return lr_scheduler

    @property
    def checkpoint(self):
        """Checkpoint callback."""
        checkpoint = tf.keras.callbacks.ModelCheckpoint(
            filepath=self.tmp_path,
            monitor='val_accuracy',
            mode='max',
            verbose=1,  # TODO? logging?
            save_best_only=True)
        return checkpoint

    def unfreeze_pretrained_model(self):
        """Unfreezes frozen layers."""
        self.model.trainable = True

    def _set_optimization_parameters(self, kwd):
        """Sets optimizer, loss and metrics."""
        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(**kwd),
            loss='categorical_crossentropy',
            metrics='accuracy',
        )

    def _restore_best_model(self):
        """Recovers best model from previous training and delete corresponding file."""
        self.model = tf.keras.models.load_model(self.tmp_path)
        os.remove(self.tmp_path)


if __name__ == '__main__':

    logging.info('\n=========\nLOAD DATA\n=========\n')

    train_generator, validation_generator = train_validation_data_generator()

    logging.info('\n============\nMAKING MODEL\n============\n')

    custom_model = CustomModel(len(config.CLASSES))
    custom_model = ModelTraining(custom_model.model)

    logging.info('\n=====\nTRAIN\n=====\n')

    custom_model.train(train_generator=train_generator,
                       validation_generator=validation_generator,
                       epochs=config.EPOCHS,
                       kwd={'learning_rate': custom_model.learning_rate_scheduler})

    logging.info('\n===========\nFINE TUNING\n===========\n')

    custom_model.unfreeze_pretrained_model()
    custom_model.train(train_generator=train_generator,
                       validation_generator=validation_generator,
                       epochs=config.EPOCHS_RETRAIN,
                       kwd={'learning_rate': config.FINE_TUNING_LEARNING_RATE})

    logging.info('\n============\nSAVING MODEL\n============\n')

    trained_model_path = os.path.join(config.MODEL_DIR, config.TRAINED_MODEL_FILENAME)
    custom_model.save(trained_model_path)
