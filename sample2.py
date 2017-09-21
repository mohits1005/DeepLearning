# These are all the modules we'll be using later. Make sure you can import them
# before proceeding further.
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import tarfile
from IPython.display import display, Image
from scipy import ndimage
from sklearn.linear_model import LogisticRegression
from six.moves.urllib.request import urlretrieve
from six.moves import cPickle as pickle

url = 'https://commondatastorage.googleapis.com/books1000/'
last_percent_reported = None
data_root = '.' # Change me to store data elsewhere

num_classes = 10
np.random.seed(133)

train_folders = ['./notMNIST_large/A', './notMNIST_large/B', './notMNIST_large/C', './notMNIST_large/D', './notMNIST_large/E', './notMNIST_large/F', './notMNIST_large/G', './notMNIST_large/H', './notMNIST_large/I', './notMNIST_large/J']
#print("train_folders ", train_folders)

test_folders = ['./notMNIST_small/A', './notMNIST_small/B', './notMNIST_small/C', './notMNIST_small/D', './notMNIST_small/E', './notMNIST_small/F', './notMNIST_small/G', './notMNIST_small/H', './notMNIST_small/I', './notMNIST_small/J']
#print("test_folders ", test_folders)

image_size = 28  # Pixel width and height.
pixel_depth = 255.0  # Number of levels per pixel.

train_datasets = []
for folder in train_folders:
    set_filename = folder + '.pickle'
    train_datasets.append(set_filename)

test_datasets = []
for folder in test_folders:
    set_filename = folder + '.pickle'
    test_datasets.append(set_filename)
