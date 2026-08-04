import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
print("Array 1:", arr1)

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Indexing
print("First element:", arr1[0])
print("Last element:", arr1[-1])
print("Slice (1 to 3):", arr1[1:4])

# Mathematical operations
print("Sum of array:", np.sum(arr1))
print("Mean of array:", np.mean(arr1))
print("Max value:", np.max(arr1))
print("Min value:", np.min(arr1))

# Array arithmetic
arr3 = np.array([10, 20, 30, 40, 50])
print("Addition:", arr1 + arr3)
print("Multiplication:", arr1 * 2)

# Array shape
print("Shape of 2D array:", arr2.shape)