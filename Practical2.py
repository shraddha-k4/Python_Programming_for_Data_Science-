
import numpy as np

# Engineering data: readings from three sensors
data = np.array([
    [12, 15, 14],
    [18, 17, 19],
    [21, 20, 22]
])

# Display original data
print("Engineering Data (Sensor Readings):")
print(data)

# Matrix operations
print("\nTranspose of matrix:")
print(data.T)

print("\nMatrix + 2:")
print(data + 2)

print("\nMatrix multiplied by 3:")
print(data * 3)

print("\nMatrix multiplication (data x transpose):")
print(np.dot(data, data.T))

# Statistical operations
print("\nMean:", np.mean(data))
print("Median:", np.median(data))
print("Standard deviation:", round(np.std(data), 2))
print("Minimum value:", np.min(data))
print("Maximum value:", np.max(data))

# Row-wise and column-wise mean
print("Column-wise mean:", np.mean(data, axis=0))
print("Row-wise mean:", np.mean(data, axis=1))
