import numpy as np

array = np.array([1, 2, 3, 4, 10])


print("\n arithmetic operators \n")  # element-wise

print(array+1)
print(array-1)
print(array*2)
print(array/2)
print(array**2)

print("\n comparison operators \n")  # element-wise

print(array == 4)
print(array > 3)

print("\n filtered atributions \n")  # bool arrays can be used to filter atributions

array[[False, True, False, True, False]] = 25
print(array)
array[array < 8] = 0
print(array)


print("\n mathematical methods \n")

print(np.sqrt(array))
print(np.round(np.sqrt(array)))

print("\n constants \n")

print(np.pi)
print(np.e)
