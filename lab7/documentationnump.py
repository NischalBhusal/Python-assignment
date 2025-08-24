import numpy as np

# 1. Array Creation
# np.array(): Create an array from a list or tuple.
arr = np.array([1, 2, 3])
print("Array:", arr)

# np.zeros(): Create an array filled with zeros.
zeros = np.zeros((2, 3))
print("Zeros Array:", zeros)

# np.ones(): Create an array filled with ones.
ones = np.ones((2, 3))
print("Ones Array:", ones)

# np.arange(): Create an array with a range of values.
range_arr = np.arange(0, 10, 2)
print("Range Array:", range_arr)

# np.linspace(): Create an array with evenly spaced values.
linspace_arr = np.linspace(0, 1, 5)
print("Linspace Array:", linspace_arr)

# 2. Array Manipulation
# np.reshape(): Reshape an array.
reshaped = np.reshape(np.arange(6), (2, 3))
print("Reshaped Array:", reshaped)

# np.transpose(): Transpose an array.
transposed = np.transpose(np.array([[1, 2], [3, 4]]))
print("Transposed Array:", transposed)

# 3. Mathematical Operations
# np.add(): Add arrays element-wise.
sum_arr = np.add([1, 2], [3, 4])
print("Sum Array:", sum_arr)

# np.subtract(): Subtract arrays element-wise.
diff_arr = np.subtract([1, 2], [3, 4])
print("Difference Array:", diff_arr)

# np.multiply(): Multiply arrays element-wise.
prod_arr = np.multiply([1, 2], [3, 4])
print("Product Array:", prod_arr)

# np.divide(): Divide arrays element-wise.
div_arr = np.divide([1, 2], [3, 4])
print("Division Array:", div_arr)

# 4. Statistical Functions
# np.mean(): Compute the mean.
mean_val = np.mean([1, 2, 3])
print("Mean:", mean_val)

# np.median(): Compute the median.
median_val = np.median([1, 2, 3])
print("Median:", median_val)

# np.std(): Compute the standard deviation.
std_val = np.std([1, 2, 3])
print("Standard Deviation:", std_val)

# np.var(): Compute the variance.
var_val = np.var([1, 2, 3])
print("Variance:", var_val)

# 5. Linear Algebra
# np.dot(): Compute the dot product.
dot_product = np.dot([1, 2], [3, 4])
print("Dot Product:", dot_product)

# np.linalg.inv(): Compute the inverse of a matrix.
matrix = np.array([[1, 2], [3, 4]])
inv_matrix = np.linalg.inv(matrix)
print("Inverse Matrix:", inv_matrix)

# 6. Random Numbers
# np.random.rand(): Generate random numbers from a uniform distribution.
rand_uniform = np.random.rand(2, 3)
print("Random Uniform Array:", rand_uniform)

# np.random.randn(): Generate random numbers from a normal distribution.
rand_normal = np.random.randn(2, 3)
print("Random Normal Array:", rand_normal)

# 7. Logical Operations
# np.all(): Test if all elements are true.
all_true = np.all([True, True])
print("All True:", all_true)

# np.any(): Test if any element is true.
any_true = np.any([True, False])
print("Any True:", any_true)