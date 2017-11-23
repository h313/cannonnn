#!/usr/bin/env python3
"""The primary file that builds and trains the neural network.

This script assumes that convert.py has been run and Skott1.csv to
Skott20.csv are in training/ and Skott21.csv to Skott25.csv are in
test/
"""
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np

# Generate dataset
train_data = np.swapaxes(np.genfromtxt('./data.csv', delimiter=','), 0, 1)
train_X = np.swapaxes(np.array([train_data[0], train_data[1], train_data[2]]), 0, 1)
train_y = np.swapaxes(np.array([train_data[3], train_data[4]]), 0, 1)

# Define the neural network
model = Sequential()

model.add(Dense(3, input_shape=(3,)))
model.add(Activation('relu'))
model.add(Dense(units=100))
model.add(Activation('softmax'))
model.add(Dense(units=500))
model.add(Activation('softmax'))
model.add(Dense(units=100))
model.add(Dense(units=2))
model.add(Activation('softmax'))

# Compile the neural network
model.compile(optimizer='adam',
              loss='poisson',
              metrics=['accuracy'])

# Fit the neural network to data
model.fit(train_X, train_y, epochs=2, batch_size=15, verbose=1, shuffle=True, validation_split=0.1)
