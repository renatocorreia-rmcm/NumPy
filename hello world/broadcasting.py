"""
	broadcasting allow numpy to
	perform operations on arrays with different shapes
	by virtually expanding dimensions to match larger array

	*the smaller dimension is expanded, not filled with 0s
"""
import numpy as np

""" COMPATIBLE ARRAYS:
	
	dimensions of same size
	OR
	one of dimensions has size 1 (so it can be expanded)
"""

a = np.array(
	[
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
)
b = np.array([10, 11, 12])  # shape (3) expands to (3, 3)  # could either be a 1 line matrix or just this 1xN vector

print(a.shape)
print(b.shape)
print(a+b)

print('\n')

a = np.array(  # shape (1, 3) will expand to (3, 3)
	[
		[1, 2, 3]
	]
)
b = np.array(  # shape (3, 1) will expand to (3, 3)
	[
		[1],
		[2],
		[3]
	]
)

print(a.shape)
print(b.shape)
print(a*b)


# exemplo de "tabuada"

a = np.array(
	[
		[1, 2, 3, 4, 5, 6, 7, 8, 9]
	]
)
b = np.array(  # shape (3, 1) will expand to (3, 3)
	[
		[1],
		[2],
		[3],
		[4],
		[5],
		[6],
		[7],
		[8],
		[9]
	]
)

print(a.shape)
print(b.shape)
print(a*b)
