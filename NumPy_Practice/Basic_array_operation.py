import numpy as np

'''
ara creation from a list
'''
ara = np.array([[1, 2, 3],
                [4, 5, 6]])
print(ara)

'''
ara creation in defined type
'''
ara = np.array([[1, 2, 3],
                [4, 5, 6]], dtype=float)
print("\n", ara)

'''
ara creation from a tuple
'''
ara = np.array(([1, 2, 3],
                [4, 5, 6]))
print("\n", ara)

'''
ara creation from a tuple of tuple
'''
ara = np.array(((1, 2, 3),
                (4, 5, 6)))
print("\n", ara)

'''
ara creation of 3X4 shaped where all elements are 0
'''
ara = np.zeros((3, 4))
print("\n", ara)

'''
ara creation of 3X4 shaped where all elements are specifice value
here specific element is 6
'''
ara = np.full((3, 4), 6)
print("\n", ara)

'''
ara creation of 3X4 shaped with random value
'''
ara = np.random.random((3, 4))
print("\n", ara)

'''
creation of 1D array with value of range(a--->b)
'''
ara = np.arange(2,3)
print("\n", ara)

'''
creation of 1D array with value of range(a--->b(c steps)
'''

ara = np.arange(0,30,5)
print("\n", ara)

'''
creation of 1D array with c elements in range (a,b) where difference
 between 2 elements will be same
'''
ara = np.linspace(0,4,10)
print("\n",ara)

ara = np.arange(1,13).reshape(3,4)
print("\n",ara)
print("\n",ara.reshape(2,3,2))
#print(ara(0,2,1))
print("\n",ara)
'''
making the array flatten that means all 
elements are being a 1D array
'''
ara = ara.flatten()
print("\n",ara)
