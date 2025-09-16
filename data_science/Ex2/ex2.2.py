# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]

import numpy as np

arr1 = np.array([0, 10, 20, 40, 60])
arr2 = np.array([10, 30, 40])

print(np.isin(arr1, arr2))