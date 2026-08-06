import matplotlib.pyplot as plt

# Data
subjects = ["Python", "NumPy", "Pandas", "ML"]
marks = [85, 90, 88, 92]

# Line Chart
plt.plot(subjects, marks, marker="o")
plt.title("Student Performance")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Bar Chart
plt.bar(subjects, marks)
plt.title("Student Performance")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Scatter Plot
hours = [1, 2, 3, 4, 5]
scores = [35, 50, 65, 80, 95]

plt.scatter(hours, scores)
plt.title("Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.show()