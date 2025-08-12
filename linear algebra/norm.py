import numpy as np

a = np.array(
	[1, 2, 2]
)


print(np.linalg.norm(a))  # computes both the norm for a vector or a matrix
print(np.linalg.vector_norm(a))  # computes the norm for a vector
