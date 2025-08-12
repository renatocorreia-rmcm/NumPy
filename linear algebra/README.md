## .linalg

numpy has some functions living in more than just 1 namespace (for usability and conveniece purposes)

some linear algebra functions are both in np.foo and np.linalg.foo (in many cases they represent the same function object in memory)

<img width="165" height="993" alt="Linear Algebra NumPy functions" src="https://github.com/user-attachments/assets/0a61f513-e5fc-4dbb-b66b-9c8cf76fe477" />

## matrices

The term matrix often indicates a 2d numpy.array object, and not a numpy.matrix object.
The latter is no longer recommended, even for linear algebra.
