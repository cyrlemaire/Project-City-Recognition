
import numpy as np
import os
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")

import src.config.config as config
from src.infrastructure.data_generator import load_test_data

if __name__ == '__main__':

    # TODO: logging 'load data'

    test_data = load_test_data()

    # TODO: logging 'load model'

    model = tf.keras.models.load_model(os.path.join(MODEL_DIR, FINAL_MODEL_NAME))

    # TODO: logging 'make predictions'

    predictions = model.predict(test_data)
    y_predictions = np.argmax(predictions, axis=1)
    class_predictions = [CLASSES[i] for i in y_predictions]
