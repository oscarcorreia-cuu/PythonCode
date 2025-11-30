import numpy as np
import time

# Define a large dataset
size = 100_000_000  # Adjust the size for comparison
python_list = list(range(size))
numpy_array = np.arange(size)

# 1. Performance Comparison: Multiplying each element by 2
print("Performance Comparison:")

# Using Python list
start = time.time()
list_result = [x * 2 for x in python_list]
end = time.time()
print(f"Python list time: {end - start:.6f} seconds")

# Using NumPy array
start = time.time()
array_result = numpy_array * 2
end = time.time()
print(f"NumPy array time: {end - start:.6f} seconds")

# 2. Memory Comparison
import sys
list_memory = sys.getsizeof(python_list)
array_memory = numpy_array.nbytes
print("\nMemory Comparison:")
print(f"Python list memory usage: {list_memory / 1024:.2f} KB")
print(f"NumPy array memory usage: {array_memory / 1024:.2f} KB")

# 3. Functionality Comparison: Calculating the mean
print("\nFunctionality Comparison:")

# Using Python list
start = time.time()
list_mean = sum(python_list) / len(python_list)
end = time.time()
print(f"Python list mean: {list_mean}, Time: {end - start:.6f} seconds")

# Using NumPy array
start = time.time()
array_mean = np.mean(numpy_array)
end = time.time()
print(f"NumPy array mean: {array_mean}, Time: {end - start:.6f} seconds")
