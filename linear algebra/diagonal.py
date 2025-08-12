import numpy as np

A = np.array(
	[
		[4,  2, 0],
		[-1, 1, 0],
		[0,  1, 2]
	]
)

print(np.linalg.diagonal(A))
print(np.linalg.diagonal(A, offset=1))
