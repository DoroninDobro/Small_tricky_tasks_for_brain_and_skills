import numpy as np

a = np.array([[30, 8, 12], [8, 30, 12], [12, 12, 10]])
b = np.array([20, 4, 8])

result = np.linalg.solve(a, b)

for i in result:
    print("{:.2f}".format(float(i)))
