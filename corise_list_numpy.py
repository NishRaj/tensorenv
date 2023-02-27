import numpy as np


python_list = list(range(5))
numpy_list = np.arange(5)
print(python_list)
print(type(numpy_list))
inclusive_start = 3
exclusive_stop = 10
numpy_arr = np.arange(inclusive_start, exclusive_stop)
print(numpy_arr)
# Linspace
inclusive_start_linspace = 15
inclusive_end = 30
num_of_elements = 10
print(np.linspace(inclusive_start_linspace, inclusive_end, num_of_elements, dtype=int))

# Size of a numpy array
size = (1, 2, 3)
print(np.random.random_sample(size))
print(np.full((1, 2, 4), -100))
