
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

# Training schedule
INITIAL_LEARNING_RATE=0.001
FINAL_LEARNING_RATE=0.00001
DECAY_STEPS=1000

# Data scrapping (only if you want to scrap new images from google image)
DRIVER_PATH = '/Users/cyrillemaire/Documents/Yotta/Project/Project_2/Chrome_drivers/chromedriver' #"path/to/google chrome/drivers"
IMAGES_PATH = '/Users/cyrillemaire/Documents/Yotta/Project/Project_2/pictures' #"path/to/download/folder"
N_IMAGES = 100 #number of image downloaded per query
QUERIES = ['facade paris',
           'building front paris',
           'maison typique Paris',
           'typical house Paris',
           'logement Paris',
           'housing Paris',
           'batiment Paris',
           'building Paris',
           'house Paris',
           'maison Paris'] #exemple of queries for Paris


