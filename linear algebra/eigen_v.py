import numpy as np

A = np.array(
	[
		[4,  2, 0],
		[-1, 1, 0],
		[0,  1, 2]
	]
)

eig_result = np.linalg.eig(A)  # get object containg values and vectors

print("\neig_result object")
print(eig_result)

print("\neigen values")
print(eig_result.eigenvalues)
print("\neigen vectors")
print(eig_result.eigenvectors)

print("\neigen values")
print(np.linalg.eigvals(A))  # get only values
