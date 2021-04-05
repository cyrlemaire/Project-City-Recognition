
import logging
import numpy as np
import os
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")

import src.config.config as config
from src.infrastructure.data_generator import load_test_data

logging.basicConfig(format='%(message)s', level=logging.INFO)

if __name__ == '__main__':

    logging.info('\n=========\nLOAD DATA\n=========\n')

    test_data = load_test_data()

    logging.info('\n==========\nLOAD MODEL\n==========\n')

    model = tf.keras.models.load_model(os.path.join(MODEL_DIR, FINAL_MODEL_NAME))

    logging.info('\n================\nMAKE PREDICTIONS\n================\n')

    predictions = model.predict(test_data)
    y_predictions = np.argmax(predictions, axis=1)
    class_predictions = [CLASSES[i] for i in y_predictions]
