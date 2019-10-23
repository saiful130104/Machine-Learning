import numpy as np

ara = np.array([1, 4, 5, 9])
print(ara)

'''
ara = ara+x // x will be added with all elements of ara
also ara-x,ara*x,ara/x,ara**x are subtract,multiply,divide 
exponent with x respectively
'''
print("\n",ara+1)
print("\n",ara-1)
print("\n",ara*2)
print("\n",ara/2)
print("\n",ara**2)
print("\n",ara**.5)

ara = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])

print("\nOriginal ara is :\n",ara)
print("\nTranspose of ara is :\n",ara.T)