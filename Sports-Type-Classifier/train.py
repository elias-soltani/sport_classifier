# set the matplotlib backend so figures can be saved in the background. Because we don't want to display the figures while running,
# we will save them instead. Agg is the backend for this, there are other backends as well.
import matplotlib
matplotlib.use("Agg")

# import data manipulation packages
import numpy as np
from sklearn.utils import shuffle
from sklearn.metrics import classification_report

# import ML and model packages
from tensorflow import keras
from tensorflow
