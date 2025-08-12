import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(type(arr))  # N dimensional array

print(arr*2)   # operator '*' implemented as element-wise

print(arr.ndim)  # number of dimentions (amount of nestings) (is about the structure/shape of data in memory)
print(arr.shape)  # size of each dimention

print(arr[0][1])  # chain indexing - slower
print(arr[0, 1])  # multidimensional indexing - faster

