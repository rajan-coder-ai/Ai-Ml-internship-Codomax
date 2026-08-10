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

# Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions on Test Data
test_predictions = model.predict(X_test)
print("Test Study Hours:", X_test.flatten())
print("Actual Scores:", y_test)
print("Predicted Scores:", test_predictions)

# Predictions on New/Unseen Data
new_study_hours = np.array([2.5, 5.5, 8.5, 11, 12]).reshape(-1, 1)
new_predictions = model.predict(new_study_hours)

print("\n--- Predictions for New Students ---")
for hours, pred in zip(new_study_hours.flatten(), new_predictions):
    print(f"Study Hours: {hours} -> Predicted Score: {pred:.2f}")
    