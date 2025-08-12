import numpy as np

print("\n rng \n")

rng = np.random.default_rng()  # may pass a seed. default is a random one. passing the same seed will lead to generate the same results every execution. sometimes may be useful
print(rng.integers(low=1, high=10, size=3))  # (inclusive, exclusive, size of vector)  # default size=1 -> scalar
print(rng.integers(low=1, high=10, size=(3, 2)))  # size also defines shape if pass tuple

print("\n uniform \n")

print(np.random.uniform(low=-1, high=-1))  # uniform distribution. each value has the same chance

print("\n shuffle \n")

arr = np.array([1, 2, 3, 4, 5])
print(arr)
np.random.shuffle(arr)  # doesnt return anything
print(arr)

print("\n random choice \n")

arr = np.array(["banana", "apple", "coconut"])
print(rng.choice(arr, size=(3, 2)))
