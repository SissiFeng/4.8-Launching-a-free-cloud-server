import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Create a mock materials dataset
np.random.seed(42)
n_samples = 1000

data = pd.DataFrame({
    'composition_A': np.random.uniform(0, 1, n_samples),
    'composition_B': np.random.uniform(0, 1, n_samples),
    'processing_temp': np.random.uniform(500, 1500, n_samples),
    'processing_time': np.random.uniform(1, 10, n_samples),
    'hardness': np.random.uniform(100, 1000, n_samples)
})

# Adjust hardness based on features to create a relationship
data['hardness'] += (data['composition_A'] * 200 + 
                     data['composition_B'] * 100 + 
                     data['processing_temp'] * 0.1 + 
                     data['processing_time'] * 10)

# Save the dataset for reference
data.to_csv('materials_data.csv', index=False)

# TODO: Load the dataset from the CSV file
# Hint: Use pd.read_csv()

# TODO: Prepare features (X) and target (y)
# Hint: Select appropriate columns for X and y

# TODO: Split the data into training and testing sets
# Hint: Use train_test_split function

# TODO: Create and train the model
# Hint: Initialize RandomForestRegressor and use its fit method

# TODO: Evaluate the model
# Hint: Use the model to predict on X_test and calculate mean squared error

# TODO: Save the model
# Hint: Use joblib.dump()

print("Model training completed and saved.")
