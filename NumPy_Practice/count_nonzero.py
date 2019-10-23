import numpy as np

ara = np.array([[ 0,  1,  2,  3],
                 [ 4,  0,  6,  7],
                 [ 8,  9, 0, 11]])
print(ara,"\n")
print(np.count_nonzero(ara),"\n")
print(np.count_nonzero(ara,axis=0),"\n")
print(np.count_nonzero(ara,axis=1),"\n")