from keras.models import Sequential
from keras.layers import Dense, Dropout

class DeepQ:

    def __init__(self, input_dimension, output_dimension, model=None):
        self.input_dimension = input_dimension
        self.output_dimension = output_dimension

        #if no model is passed as parameter, create default model
        if model != None:
            self.model = self._createModel(self)
        else:
            self.model = model

    def _createModel(self):
        #Default model
        model = Sequential()
        model.add(Dense(24, input_dim=input_dim, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(output_dim, activation='softmax'))
        model.compile(loss='mse', optimizer=Adam(lr=0.001))
        return model