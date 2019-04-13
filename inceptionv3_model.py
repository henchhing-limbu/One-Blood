# importing required modules
from keras.applications import InceptionV3
from keras.models import Model
from keras.models import Sequential
from keras.layers import Activation, Dense
import keras

# creating bottleneck model
original_model    = InceptionV3()
bottleneck_input  = original_model.get_layer(index=0).input
bottleneck_output = original_model.get_layer(index=-2).output
bottleneck_model  = Model(inputs=bottleneck_input, outputs=bottleneck_output)

# setting the weights of bottleneck model to be constant
for layer in bottleneck_model.layers:
    layer.trainable = False

# Creating a sequential model that uses pretrained model (bottleneck_model)
new_model = Sequential()
new_model.add(bottleneck_model)
new_model.add(Dense(4, activation='softmax', input_dim=2048))

# TODO: need to make it work for multi-class problem
# For a binary classification problem
new_model.compile(optimizer='rmsprop',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
# TODO: labels and input needed
# TODO: Datapreprocessing needed here
one_hot_labels = keras.utils.to_categorical(labels, num_classes=2)
new_model.fit(processed_imgs_array,
              one_hot_labels,
              epochs=2,
              batch_size=32)