from keras.layers import Input, Dense
from keras.models import Model
import input_data
# this returns a tensor
inputs = Input(shape=(784,))

# a layer instance is callable on a tensor, and returns a tensor
x = Dense(64, activation='relu')(inputs)
x = Dense(64, activation='relu')(x)
predictions = Dense(10, activation='softmax')(x)

# this creates a model that includes
# the Input layer and three Dense layers
model = Model(input=inputs, output=predictions)
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

trainNumber = 5000
testNumber  = 2000
mnist = input_data.read_data_sets("../MNIST_data/", one_hot=True)
x_train, y_train, x_test, y_test = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels
print "x_train.shape = ",x_train.shape
x_train = x_train[0:trainNumber]
y_train = y_train[0:trainNumber]
x_test = x_test[0:testNumber]
y_test = y_test[0:testNumber]
print "x_train.shape = ",x_train.shape
model.fit(x_train, y_train)  # starts training