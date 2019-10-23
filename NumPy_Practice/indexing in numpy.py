import numpy as np

ara = np.array([[ 1, 2, 3, 4, 5],
                 [ 6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20]])
print(ara)
'''
indexing array in normal way
'''
print("\n",ara[0,0],ara[1,1],ara[2,2],ara[3,3])
'''
indexing array in advanced way
'''
print("\n",ara[[0,1,2,3],[0,1,2,3]])
'''
boolean ara generation
'''
indexes = ara>9
print("\n",indexes)
print("\n",ara[indexes])
'''
the above process can also be done like bellow
'''
print("\n",ara[ara>9])