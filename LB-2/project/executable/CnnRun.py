import pickle

import numpy as np
from timeit import default_timer as timer
from tensorflow.python.keras import Sequential, optimizers
from tensorflow.python.keras.layers import Conv1D, BatchNormalization, Dropout, Flatten, Dense

from project.PathConstants import PathConstants

LR = 0.0009 # maybe after some (10-15) epochs reduce it to 0.0008-0.0007
drop_out = 0.38
batch_dim = 1024
nn_epochs = 100

loss = 'categorical_crossentropy' # best standart

def cnn_model():
    m = Sequential()
    m.add(Conv1D(128, 5, padding='same', activation='relu', input_shape=(340, 1)))
    m.add(BatchNormalization())
    m.add(Dropout(drop_out))
    m.add(Conv1D(128, 3, padding='same', activation='relu'))
    m.add(BatchNormalization())
    m.add(Dropout(drop_out))
    m.add(Conv1D(64, 3, padding='same', activation='relu'))
    m.add(BatchNormalization())
    m.add(Dropout(drop_out))
    m.add(Flatten())
    m.add(Dense(128, activation='relu'))
    m.add(Dense(32, activation='relu'))
    m.add(Dense(3, activation = 'softmax'))
    opt = optimizers.Adam(lr=LR)
    m.compile(optimizer=opt,
              loss=loss,
              metrics=['accuracy', 'mae'])

    print("\nHyper Parameters\n")
    print("Learning Rate: " + str(LR))
    print("Drop out: " + str(drop_out))
    print("Batch dim: " + str(batch_dim))
    print("Number of epochs: " + str(nn_epochs))
    print("\nLoss: " + loss + "\n")

    m.summary()

    return m


if __name__ == '__main__':

    start_time = timer()
    model = cnn_model()
    dump_profile = PathConstants.dump_svm_profile_template.format(0)
    with open(dump_profile, 'rb') as file:
        profile = pickle.load(file)
    x_train = profile.x_train
    x_train = np.expand_dims(x_train, axis=2)
    y_train = profile.y_train
    history = model.fit(x_train, y_train, epochs=nn_epochs, batch_size=len(x_train))
    end_time = timer()
    print("Time elapsed: " + "{0:.2f}".format((end_time - start_time)) + " s")
