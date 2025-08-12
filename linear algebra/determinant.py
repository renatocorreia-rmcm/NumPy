import numpy as np

A = np.array(
	[
		[4,  2, 0],
		[-1, 1, 0],
		[0,  1, 2]
	]
)

print(np.linalg.det(A))

print('\n')
slogdet_result = np.linalg.slogdet(A)  # useful for very small/large dets  (more roboust against under/overflow)
print(slogdet_result)
print(slogdet_result.sign)  # -1, 0, 1
print(slogdet_result.logabsdet)  # natural log of det
