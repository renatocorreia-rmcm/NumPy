import numpy as np

array = np.array([
	[1,  2,  3,  4],
	[5,  6,  7,  8],
	[9,  10, 11, 12],
	[13, 14, 15, 16]
])

# array[start:end:step]
# is possible to combine chain and multidimensional indexing
print(array[:, 1])  # all rows, column 1
print(array[:, :2])  # all rows, columns 0-2

"""
	np arr '[]' operator take kwargs, one iterator for each dimention
	this iterator can be either the index itself or the start:stop:step format
"""
