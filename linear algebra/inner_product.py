"""
	1-D vectors: ordinary inner product
	N-D vectors: sum product over the last axes
"""

import numpy as np

a = np.array(
	[1, 2, 3]
)
b = np.array(
	[4, 5, 6]
)

print(np.inner(a, b))
