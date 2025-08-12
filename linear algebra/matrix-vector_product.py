import numpy as np

A = np.array(
	[
		[1, 2, 1],
		[3, 4, 2],
		[5, 6, 3]
	]
)
b = np.array(
	[1, 2, 3]
)

print(np.matvec(A, b))
