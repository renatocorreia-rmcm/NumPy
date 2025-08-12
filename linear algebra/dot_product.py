"""
	a and b dimensions:
	0-D (scalars)  -> is preferred to a*b
	1-D (vectors)  -> vectorial inner product - APPROPRIATE CASE
	2-D (matrices) -> is prefered to a@b
"""
import numpy as np

a = np.array(
	[1, 2, 3]
)
b = np.array(
	[4, 5, 6]
)

print(np.dot(a, b))
