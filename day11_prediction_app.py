# Day 11 - Prediction App

from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
scores = np.array([35, 40, 50, 55, 60, 70, 75, 85])

# Create and train model
model = LinearRegression()
model.fit(study_hours, scores)

# User input
hours = float(input("Enter study hours: "))

# Prediction
prediction = model.predict([[hours]])

print("Study Hours:", hours)
print("Predicted Score:", round(prediction[0], 2))