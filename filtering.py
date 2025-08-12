"""
	slecting elements in an array
	that match a given condition
"""

import numpy as np

arr = np.array(
	[
		[10, 2, 3],
		[9, 8, 7]
	]
)

print("\n boolean indexing \n")  # will flat array  # faster

print(arr[arr < 8])
print(arr[(arr < 9) & (arr > 3)])  # uses C boolean operator
print(arr[arr % 2 == 0])

print("\n where function \n")  # retain original shape  # slower
print(np.where((arr % 2 == 0), arr, 0))  # (condition, array, 'to-replace' if !condition)
print(np.where((arr < 8), arr, -1))  # (condition, array, 'to-replace' if !condition)
