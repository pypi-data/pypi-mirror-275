import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.holtwinters import  Holt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split
from abc import ABC, abstractmethod


# abstract class to construct others model
class Model(ABC):

    @abstractmethod
    def train(self):
        pass
    
    @abstractmethod
    def predict(self):
        pass

# Naive model
class Naive(Model):
    def __init__(self):
        self.last_observation = None

    def train(self, value):
        self.last_observation = value
    
    def predict(self):
        return self.last_observation

        

# HoltWinters model
class HoltWinters(Model):
    def __init__(self):
        self.model = None
    
    def train(self, train_df, optimized=True,smoothing_level=None, smoothing_trend=None):
        model = Holt(np.asarray(train_df['SolarPower']))
        model._index = pd.to_datetime(train_df.index)

        if optimized:
            fit = model.fit(optimized=True)
        else:
            fit = model.fit(optimized=False, smoothing_level=smoothing_level, smoothing_trend=smoothing_trend)
        self.model = fit

    def predict(self, test_df):
        if self.model:
            return self.model.forecast(test_df.shape[0])
    

class NNAR(Model):
    def __init__(self):
        self.model = None
        self.last_targets = None
        self.last_pred = None

    def train(self, df, scaler, window_size , n_nodes, epochs):
        scaled_data = scaler.fit_transform(df.values.reshape(-1, 1))

        # Define window size for lagged features
        window_size = window_size  # Number of past days to consider

        # Create features and target
        features = []
        targets = []
        for i in range(window_size, len(scaled_data)):
            features.append(scaled_data[i - window_size:i, 0])
            targets.append(scaled_data[i, 0])

        features, targets = np.array(features), np.array(targets)

        # Train-Validation-Test Split
        train_features, test_features, train_targets, test_targets = train_test_split(features, targets, test_size=0.2, shuffle=False)
        train_features, val_features, train_targets, val_targets = train_test_split(train_features, train_targets, test_size=0.1, shuffle=False)

        # Reshape features for LSTM
        train_features = train_features.reshape(-1, train_features.shape[1], 1)
        val_features = val_features.reshape(-1, val_features.shape[1], 1)
        test_features = test_features.reshape(-1, test_features.shape[1], 1)

        # Define and train the Neural Network Autoregression model
        model = Sequential()
        model.add(LSTM(n_nodes, return_sequences=False, input_shape=(train_features.shape[1], 1)))
        model.add(Dense(1))
        model.compile(loss="mse", optimizer="adam")
        model.fit(train_features, train_targets, epochs=epochs, validation_data=(val_features, val_targets))
        self.model = model
        self.last_targets = test_targets

    def predict(self, test_features):
        if self.model:
            test_pred = self.model.predict(test_features)
            self.last_pred = test_pred