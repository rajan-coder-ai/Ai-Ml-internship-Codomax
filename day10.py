from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Dataset - Study Hours vs Score
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
scores = np.array([35, 40, 50, 55, 65, 70, 78, 85, 90, 95])

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    study_hours, scores, test_size=0.2, random_state=42
)

# Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Model Evaluation Metrics
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("--- Model Evaluation ---")
print("Actual Scores:", y_test)
print("Predicted Scores:", predictions)
print(f"\nMean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")

print("\n--- Internship Journey Complete! ---")
print("From Python basics to a fully evaluated ML model in 10 days!")