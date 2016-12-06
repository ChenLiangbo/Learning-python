from keras.layers import Input, Dense
from keras.models import Model
from keras.models import Sequential  
from keras.layers.core import Dense, Dropout, Activation, Flatten  
from keras.layers.convolutional import Convolution2D, MaxPooling2D  
from keras.optimizers import SGD  
from keras.utils import np_utils


img_rows, img_cols = 57, 47  
 
nb_filters1, nb_filters2 = 5, 10  
 
nb_pool = 2  

nb_conv = 3  
inputs = Input(shape = (None,1,28,28))