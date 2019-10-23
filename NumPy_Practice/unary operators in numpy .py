import numpy as np

ara = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])
print("\n",ara.max())
print("\n",ara.max(axis=0))
print("\n",ara.max(axis=1))
print("\n",ara.min())
print("\n",ara.min(axis=0))
print("\n",ara.min(axis=1))
print("\n",ara.sum())
print("\n",ara.sum(axis=0))
print("\n",ara.sum(axis=1))
print("\n",ara.cumsum())
print("\n",ara.cumsum(axis=0))