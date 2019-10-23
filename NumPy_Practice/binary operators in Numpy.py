import numpy as np

arr = np.array([[1, 2],
              [3, 4]])
brr = np.array([[4, 3],
              [2, 1]])

print("\n",arr)
print("\n",brr)

'''
add operation
'''

print("\n",arr+brr)

'''
multiplication operation
'''
print("\n",arr*brr)

'''
division operation
'''
print("\n",arr/brr)

'''
matrix multiplication operation
'''
print("\n",arr.dot(brr))