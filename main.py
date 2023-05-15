import numpy as np

x1 = np.array([1, 1, 1])
x2 = np.array([2, 2, 2])

print(np.linalg.norm(x1 - x2, ord=2))
