"""
	A^(-n) = [A^(-1)]^n
"""

import numpy as np

A = np.array(
	[
		[1, 2, 3],
		[3, 1, 2],
		[1, 4, 0]
	]
)

print(np.linalg.matrix_power(A, 3))
