
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")

import src.config.config as config


class CustomModel:
    """Implements our custom architecture.

    Attributes
    ----------
    model: tf.keras.Model
    image_scaler: tf.keras.Sequential
    pretrained_model: tf.keras.Model
    specific_task_learner: tf.keras.Sequential
    """

    def __init__(self, number_classes: int):
        self.number_classes = number_classes

    @property
    def model(self):
        """Builds custom model."""
        inputs = tf.keras.Input(shape=config.IMAGE_SHAPE)
        x = self.image_scaler(inputs)
        x = self.pretrained_model(x, training=False)
        outputs = self.specific_task_learner(x)
        model = tf.keras.Model(inputs, outputs)
        return model

    @property
    def image_scaler(self):
        """Image scaler."""
        image_scaler = tf.keras.Sequential([
          tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
        ])
        return image_scaler

    @property
    def pretrained_model(self):
        """Pretrained model."""
        pretrained_model = tf.keras.applications.DenseNet201(
            weights="imagenet",
            input_shape=config.IMAGE_SHAPE,
            include_top=False,
        )
        pretrained_model.trainable = False
        return pretrained_model

    @property
    def specific_task_learner(self):
        """Final layers for specific task learning."""
        specific_task_learner = tf.keras.Sequential([
            tf.keras.layers.GlobalAveragePooling2D(),
            tf.keras.layers.Dropout(.3),
            tf.keras.layers.Dense(256),
            tf.keras.layers.Dropout(.3),
            tf.keras.layers.Dense(128),
            tf.keras.layers.Dropout(.3),
            tf.keras.layers.Dense(64),
            tf.keras.layers.Dense(self.number_classes, activation='softmax')
        ])
        return specific_task_learner
