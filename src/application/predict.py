
import os
import numpy as np
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")

from src.config.config import *
from src.infrastructure.data_loading import load_test_data

if __name__ == '__main__':

    print('=========')
    print('LOAD DATA')
    print('=========')

    test_data = load_test_data()

    print('==========')
    print('LOAD MODEL')
    print('==========')

    model = tf.keras.models.load_model(os.path.join(MODEL_DIR, MODEL_NAME))

    print('================')
    print('MAKE PREDICTIONS')
    print('================')

    pred = model.predict(test_data)
    y_pred = np.argmax(pred, axis=1)
    class_pred = [CLASSES[i] for i in y_pred]
