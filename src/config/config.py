
import os

# Directories
REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
TRAIN_DATA_DIR = os.path.join(REPO_DIR, 'data/')
TEST_DATA_DIR = TRAIN_DATA_DIR
MODEL_DIR = os.path.join(REPO_DIR, 'models/')
CHECKPOINT_DIR = os.path.join(REPO_DIR, 'checkpoint/')
CHECKPOINT_FILE_PATH = os.path.join(CHECKPOINT_DIR, 'weights.{epoch:02d}-{val_accuracy:.2f}.hdf5')

# Initialize random seed
SEED=1234567890

# Data constants
CLASSES=['Amsterdam', 'London', 'Paris', 'Strasbourg', 'Venice']
IMAGE_SHAPE=(150, 150, 3)
IMAGE_SIZE=(150, 150)
BATCH_SIZE=32
VALIDATION_SPLIT=.1
INTERPOLATION="bilinear"
D0_DATA_AUGMENTATION=True

# Training constants
EPOCHS=100
RETRAIN=True
EPOCHS_RETRAIN=10
MODEL_NAME='PCR_model'

