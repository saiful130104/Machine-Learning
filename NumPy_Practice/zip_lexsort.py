import numpy as np

ar = np.array([9, 3, 1, 3, 4, 3, 6])
br = np.array([4, 6, 9, 2, 1, 8, 7])
cr = np.array([1, 3, 7, 5, 4, 8, 9])
'''
using zip pair can be made between two arrays
''' 
my_list = [a for (a) in zip(ar, br, cr)]
print(my_list)
print("\n", sorted(my_list))
'''
lexsort is used for 
'''
print("\n", np.lexsort((br, ar)))
