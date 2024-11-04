import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Input

data = pd.read_csv('finaldataset.csv')

# Preprocessing
X = data.iloc[:, :-1].values  # Features
y = data.iloc[:, -1].values    # Labels

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Normalize features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Reshape input for LSTM [samples, time steps, features]
X_reshaped = np.reshape(X_scaled, (X_scaled.shape[0], 1, X_scaled.shape[1]))  # 1 time step for each sample

# Build LSTM model
model = Sequential()
model.add(Input(shape=(1, X_reshaped.shape[2])))  # Input layer with dynamic feature size
model.add(LSTM(50, return_sequences=True))        # LSTM layer
model.add(Dropout(0.2))                           # Dropout layer
model.add(LSTM(50))                               # Another LSTM layer
model.add(Dropout(0.2))                           # Dropout layer
model.add(Dense(len(np.unique(y_encoded)), activation='softmax'))  # Output layer with softmax for multi-class classification

# Compile model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
model.fit(X_reshaped, y_encoded, epochs=100, batch_size=32)

# Function to predict crop based on new conditions (any number of features)
def predict_crop(new_conditions):
    # Pad with zeros if fewer features are provided or truncate if more are given
    expected_features = X_reshaped.shape[2]  # Number of features the model was trained on
    
    if len(new_conditions) < expected_features:
        new_conditions = np.concatenate([new_conditions, np.zeros(expected_features - len(new_conditions))])
    elif len(new_conditions) > expected_features:
        new_conditions = new_conditions[:expected_features]
    
    
    # Scale the input conditions
    new_conditions_scaled = scaler.transform([new_conditions])
    
    # Reshape for LSTM input: [samples, time steps, features]
    new_conditions_reshaped = np.reshape(new_conditions_scaled, (1, 1, len(new_conditions_scaled[0])))
    
    # Make prediction
    prediction = model.predict(new_conditions_reshaped)
    
    # Decode the predicted label (numeric to crop name)
    predicted_crop = label_encoder.inverse_transform([np.argmax(prediction)])
    
    return predicted_crop[0]

# Example with 7 features
new_conditions = [90, 40, 50, 25.0, 60.0, 6.5, 100.0]  # You can pass any number of features
recommended_crop = predict_crop(new_conditions)
print(f"The recommended crop is: {recommended_crop}")
