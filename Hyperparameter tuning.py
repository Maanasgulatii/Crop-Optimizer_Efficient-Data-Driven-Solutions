import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense
from keras_tuner import HyperModel, RandomSearch
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load your dataset
data = pd.read_csv('finaldataset.csv')

# Fill missing values if any
if data.isnull().sum().any():
    data.fillna(data.mean(), inplace=True)  # Fill missing values with mean

# Convert categorical labels to numerical values
label_encoder = LabelEncoder()
data['label'] = label_encoder.fit_transform(data['label'])

# Prepare your features and labels
features = data[['N', 'P', 'K', 'temperature', 'humidity']].values
labels = data['label'].values

# Define timesteps and reshape data for LSTM
timesteps = 10  # Number of timesteps (adjust if needed)

# Create sequences for time series
def create_sequences(X, y, timesteps):
    Xs, ys = [], []
    for i in range(len(X) - timesteps):
        Xs.append(X[i:i + timesteps])
        ys.append(y[i + timesteps])
    return np.array(Xs), np.array(ys)

# Create sequences for features and labels
X_seq, y_seq = create_sequences(features, labels, timesteps)

# Split into training and validation sets (80/20 split)
X_train, X_val, y_train, y_val = train_test_split(X_seq, y_seq, test_size=0.2, random_state=42)

# HyperModel for LSTM tuning
class LSTMHyperModel(HyperModel):
    def build(self, hp):
        model = Sequential()
        model.add(LSTM(units=hp.Int('units', min_value=32, max_value=256, step=32), 
                       return_sequences=True, input_shape=(timesteps, features.shape[1])))
        model.add(Dropout(rate=hp.Float('dropout', 0.2, 0.5, step=0.1)))
        model.add(LSTM(units=hp.Int('units2', min_value=32, max_value=256, step=32)))
        model.add(Dropout(rate=hp.Float('dropout2', 0.2, 0.5, step=0.1)))
        model.add(Dense(1, activation='sigmoid'))

        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

# Initialize the tuner with explicit n_init to suppress warnings
tuner = RandomSearch(LSTMHyperModel(), objective='val_accuracy', max_trials=7)

# Search for the best hyperparameters
tuner.search(X_train, y_train, epochs=50, validation_data=(X_val, y_val))
