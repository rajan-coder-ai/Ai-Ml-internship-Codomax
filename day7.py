from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data - Study Hours vs Score
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
scores = np.array([35, 40, 50, 55, 65, 70, 78, 85, 90, 95])

print("Study Hours:\n", study_hours.flatten())
print("Scores:\n", scores)

# Train-Test Split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    study_hours, scores, test_size=0.2, random_state=42
)

print("\nTraining Data Size:", len(X_train))
print("Testing Data Size:", len(X_test))

# Create and train a simple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Coefficient (slope):", model.coef_[0])
print("Model Intercept:", model.intercept_)

# Concept explanation
print("\n--- Supervised Learning Concept ---")
print("We have input features (Study Hours) and known output labels (Scores).")
print("The model learns the relationship between them during training.")
print("Train-test split helps us evaluate the model on unseen data.")