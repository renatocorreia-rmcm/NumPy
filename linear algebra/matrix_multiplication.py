"""
	N-D arguments are treated as a stack of matrices residing in the last 2 axis
"""
import numpy as np

A = np.array(
	[
		[1, 2],
		[3, 4],
		[5, 6]
	]
)
B = np.array(
	[
		[1, 2, 3],
		[4, 5, 6]
	]
)

print(A@B)  # implemented by np.matmul()
