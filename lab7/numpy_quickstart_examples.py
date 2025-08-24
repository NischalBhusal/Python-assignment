# NumPy Quickstart Examples
# This file contains examples from the official NumPy quickstart guide: https://numpy.org/doc/stable/user/quickstart.html

import numpy as np

# 1. The Basics
# Create an array
array = np.array([1, 2, 3, 4])
print("Array:", array)

# Create a multidimensional array
multi_array = np.array([[1, 2], [3, 4]])
print("Multidimensional Array:", multi_array)

# Check the shape of the array
print("Shape:", multi_array.shape)

# Create an array with a specific data type
float_array = np.array([1, 2, 3], dtype=float)
print("Float Array:", float_array)

# 2. Array Creation
# Create an array of zeros
zeros = np.zeros((2, 3))
print("Zeros Array:", zeros)

# Create an array of ones
ones = np.ones((2, 3))
print("Ones Array:", ones)

# Create an empty array
empty = np.empty((2, 3))
print("Empty Array:", empty)

# Create an array with a range of values
arange = np.arange(0, 10, 2)
print("Arange Array:", arange)

# Create an array with evenly spaced values
linspace = np.linspace(0, 1, 5)
print("Linspace Array:", linspace)

# 3. Basic Operations
# Element-wise addition
addition = np.array([1, 2, 3]) + np.array([4, 5, 6])
print("Addition:", addition)

# Element-wise multiplication
multiplication = np.array([1, 2, 3]) * np.array([4, 5, 6])
print("Multiplication:", multiplication)

# Matrix multiplication
matrix_mult = np.dot(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))
print("Matrix Multiplication:", matrix_mult)

# 4. Universal Functions
# Compute the sine of an array
sine = np.sin(np.pi / 2)
print("Sine:", sine)

# Compute the exponential of an array
exponential = np.exp([1, 2, 3])
print("Exponential:", exponential)

# Compute the square root of an array
sqrt = np.sqrt([1, 4, 9])
print("Square Root:", sqrt)

# 5. Indexing, Slicing, and Iterating
# Indexing
indexing = np.array([1, 2, 3, 4, 5])[2]
print("Indexing:", indexing)

# Slicing
slicing = np.array([1, 2, 3, 4, 5])[1:4]
print("Slicing:", slicing)

# Iterating
iterating = [x for x in np.array([1, 2, 3])]
print("Iterating:", iterating)

# 6. Shape Manipulation
# Reshape an array
reshaped = np.arange(6).reshape((2, 3))
print("Reshaped Array:", reshaped)

# Transpose an array
transposed = reshaped.T
print("Transposed Array:", transposed)

# 7. Stacking and Splitting
# Stack arrays vertically
vstack = np.vstack((np.array([1, 2]), np.array([3, 4])))
print("Vertical Stack:", vstack)

# Stack arrays horizontally
hstack = np.hstack((np.array([1, 2]), np.array([3, 4])))
print("Horizontal Stack:", hstack)

# Split an array
split = np.hsplit(np.array([[1, 2, 3], [4, 5, 6]]), 3)
print("Split Array:", split)

# 8. Copies and Views
# Create a view of an array
original = np.array([1, 2, 3])
view = original.view()
view[0] = 99
print("Original Array:", original)
print("View Array:", view)

# Create a copy of an array
copy = original.copy()
copy[0] = 0
print("Original Array After Copy:", original)
print("Copy Array:", copy)

# 9. Linear Algebra
# Compute the inverse of a matrix
matrix = np.array([[1, 2], [3, 4]])
inverse = np.linalg.inv(matrix)
print("Inverse Matrix:", inverse)

# Compute the eigenvalues of a matrix
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

# Solve a linear system of equations
coefficients = np.array([[3, 1], [1, 2]])
constants = np.array([9, 8])
solution = np.linalg.solve(coefficients, constants)
print("Solution:", solution)
