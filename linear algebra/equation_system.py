"""
	A * x = b
"""

import numpy as np

A = np.array(
	[
		[4,  2, 0],
		[-1, 1, 0],
		[0,  1, 2]
	]
)
b = np.array(
	[1, 2, 3]
)

x = np.linalg.solve(A, b)
print(x)
print(np.allclose(np.dot(A, x), b))
