import pandas as pd
import numpy as np

# Creating a sample dataset with missing values and duplicates
data = {
    'StudentName': ['Rajan', 'Aman', 'Priya', 'Sara', 'Vikram', 'Priya'],
    'StudyHours': [5, 3, np.nan, 2, 6, 7],
    'Score': [85, 65, 92, np.nan, 88, 92]
}

df = pd.DataFrame(data)

print("Original Dataset:\n", df)

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Handle missing values (fill with mean)
df['StudyHours'] = df['StudyHours'].fillna(df['StudyHours'].mean())
df['Score'] = df['Score'].fillna(df['Score'].mean())

print("\nAfter Filling Missing Values:\n", df)

# Check for duplicates
print("\nDuplicate Rows:\n", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:\n", df)

# Dataset statistics
print("\nDataset Statistics:\n", df.describe())