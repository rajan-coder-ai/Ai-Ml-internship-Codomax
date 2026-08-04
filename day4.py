import pandas as pd

# Creating a sample student score dataset
data = {
    'StudentName': ['Rajan', 'Aman', 'Priya', 'Sara', 'Vikram'],
    'StudyHours': [5, 3, 7, 2, 6],
    'Score': [85, 65, 92, 55, 88]
}

df = pd.DataFrame(data)

# Save it as CSV for future use
df.to_csv('student_scores.csv', index=False)

# Load the dataset
df = pd.read_csv('student_scores.csv')

# Explore the dataset
print("First 5 rows:\n", df.head())
print("\nDataset Shape (rows, columns):", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nDataset Info:")
print(df.info())
print("\nBasic Statistics:\n", df.describe())