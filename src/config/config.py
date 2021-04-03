
import os

# Directories
REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
TRAIN_DATA_DIR = os.path.join(REPO_DIR, 'data/')
TEST_DATA_DIR = TRAIN_DATA_DIR
MODEL_DIR = os.path.join(REPO_DIR, 'models/')
TRAINED_MODEL_FILENAME='trained_model.hdf5'
FINAL_MODEL_FILENAME='PCR_model.hdf5'

# Initialize random seed
SEED=1234567890

# Data constants
CLASSES=['Amsterdam', 'London', 'Paris', 'Strasbourg', 'Venice']
IMAGE_SHAPE=(150, 150, 3)
IMAGE_SIZE=(150, 150)
BATCH_SIZE=64
VALIDATION_SPLIT=.1
INTERPOLATION="bilinear"

# Training constants
EPOCHS=100
EPOCHS_RETRAIN=10

# Training schedule
INITIAL_LEARNING_RATE=0.001
FINAL_LEARNING_RATE=0.0001
DECAY_STEPS=1000
FINE_TUNING_LEARNING_RATE=1.3e-5
