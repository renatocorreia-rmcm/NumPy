"""
	outer(v1, v2) = v1 * tranposed(v2)
	is the product between all possible combinations of v1_i and v2_j
"""

import numpy as np

a = np.array(
	[1, 2, 3]
)
b = np.array(
	[4, 5, 6]
)

print(np.outer(a, b))
