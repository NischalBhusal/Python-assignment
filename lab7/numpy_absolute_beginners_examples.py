# NumPy Absolute Beginners Examples
# This file contains examples from the official NumPy guide for absolute beginners: https://numpy.org/devdocs/user/absolute_beginners.html

import numpy as np

# 1. Creating Arrays
# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:", array_2d)

# Create an array with a specific data type
array_float = np.array([1, 2, 3], dtype=float)
print("Float Array:", array_float)

# 2. Inspecting Arrays
# Check the shape of the array
print("Shape of 2D Array:", array_2d.shape)

# Check the data type of the array
print("Data Type of Float Array:", array_float.dtype)

# Check the size of the array
print("Size of 1D Array:", array_1d.size)

# 3. Array Operations
# Element-wise addition
addition = array_1d + 5
print("Addition:", addition)

# Element-wise multiplication
multiplication = array_1d * 2
print("Multiplication:", multiplication)

# Element-wise power
power = array_1d ** 2
print("Power:", power)

# 4. Array Indexing and Slicing
# Indexing
index = array_1d[2]
print("Indexing (3rd element):", index)

# Slicing
slice_ = array_1d[1:4]
print("Slicing (2nd to 4th elements):", slice_)

# 5. Reshaping Arrays
# Reshape a 1D array into a 2D array
reshaped = array_1d.reshape((1, 5))
print("Reshaped Array:", reshaped)

# 6. Combining Arrays
# Concatenate two arrays
concatenated = np.concatenate((array_1d, [6, 7, 8]))
print("Concatenated Array:", concatenated)

# Stack arrays vertically
vstacked = np.vstack((array_1d, [6, 7, 8, 9, 10]))
print("Vertically Stacked Array:", vstacked)

# Stack arrays horizontally
hstacked = np.hstack((array_1d, [6, 7, 8, 9, 10]))
print("Horizontally Stacked Array:", hstacked)

# 7. Splitting Arrays
# Split an array into multiple sub-arrays
split = np.array_split(array_1d, 3)
print("Split Array:", split)

# 8. Copying Arrays
# Create a copy of an array
copy = array_1d.copy()
copy[0] = 99
print("Original Array:", array_1d)
print("Copied Array:", copy)

# 9. Mathematical Functions
# Compute the mean
mean = np.mean(array_1d)
print("Mean:", mean)

# Compute the standard deviation
std = np.std(array_1d)
print("Standard Deviation:", std)

# Compute the sum
sum_ = np.sum(array_1d)
print("Sum:", sum_)

# Compute the product
product = np.prod(array_1d)
print("Product:", product)
