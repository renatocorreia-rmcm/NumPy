"""
	summarize data
	tipically return a single value
		if axis argument is not defined. if it is, return a value for each group in axis

	"as aggregation functions in SQL. 'axis' may be seen as a 'group by'"
"""

import numpy as np

arr = np.array(
	[
		[7, 9, 11],
		[1, 3,  5]
	]
)

print("\n arithmetic \n")
# sommatory
print(np.sum(arr))
print(np.sum(arr, axis=0))  # column-wise
print(np.sum(arr, axis=1))  # line-wise
# arithmetic mean
print(np.mean(arr))
print(np.mean(arr, axis=0))  # column-wise
print(np.mean(arr, axis=1))  # line-wise

print("\n statistics \n")
# standart deviation
print(np.std(arr))
# variance
print(np.var(arr))

print("\n min/max \n")
# value
print(np.min(arr))
print(np.max(arr))
# index
print(np.argmin(arr))
print(np.argmax(arr))
