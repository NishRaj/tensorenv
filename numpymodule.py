import numpy as np

# Initialize an array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
# Know the number or rows and columns in an array
print(arr.shape)

# Know the dimensions of array
print(arr.ndim)

# Access the element in the array
print(arr[0, 1])

# Append the element into an array. If axis is given then it will add based on the axis
arr = np.append(arr, [99, 999])
print(arr)

# Create a zero based array
# 2 Sets, 3 Rows per Set, 2 Columns
zero_arr = np.zeros((2, 3, 2), dtype=int)
print(zero_arr)

# Create an array using arange. First element to include, first element to exclude, step
rng_arr = np.arange(1, 9, 3)
print(rng_arr)

lin_arr = np.linspace(1., 4., 6)
print(lin_arr)

# Add two arrays
x = np.ones((2, 3), dtype=int)
y = np.random.randint(150, 1000, (2, 3), dtype='int64')
z = np.add(x, y)
print(f"Random array is y = {y}")
print(f"The dtype of random array is {y.dtype}")
print(f"The itemsize is {y.itemsize}")
print(f"The number of bytes is {y.nbytes}")
print(f"The sum is {z}")
w = np.subtract(x, y)
print(f"The subtraction is {w}")

# v = np.dot(x, y)
# print(v)

# Transpose of an array
trans_z = z.T
print(trans_z)

print(np.array([range(i, i + 3) for i in [2, 4, 6]]))
#list(range(i, i+3) for i in [2, 4, 6])
for i in [2, 4, 6]:
    print(range(i, i+3))
    print(i)