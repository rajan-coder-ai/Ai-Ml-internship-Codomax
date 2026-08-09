from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Dataset - Study Hours vs Score
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
scores = np.array([35, 40, 50, 55, 65, 70, 78, 85, 90, 95])

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    study_hours, scores, test_size=0.2, random_state=42
)

# Build and Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

print("Model training completed successfully!")
print("\nModel Coefficient (slope):", model.coef_[0])
print("Model Intercept:", model.intercept_)

# Model equation
print(f"\nModel Equation: Score = {model.coef_[0]:.2f} * StudyHours + {model.intercept_:.2f}")

# Quick check - predict on training data itself
train_predictions = model.predict(X_train)
print("\nTraining Predictions:", train_predictions)
print("Actual Training Scores:", y_train)