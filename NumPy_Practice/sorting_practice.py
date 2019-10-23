import numpy as np

ara = np.array([[1, 4, 2],
              [3, 4, 6],
              [0, -1, 5]])
print("\n",np.sort(ara))
print("\n",np.argsort(ara))
print("\n",ara)
print("\n",np.sort(ara,axis=None).reshape(3,3))
print("\n",np.sort(ara,axis=0))
print("\n",np.sort(ara,axis=1))

defined_data_type = [('name' , 'S10'),('id',int),('cgpa',float)]
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]

ara = np.array(values, dtype=defined_data_type)

print("\n",ara)
print("\n",np.sort(ara))
print("\n",np.sort(ara,order='name'))
print("\n",np.sort(ara,order=['id','name']))
print("\n",np.sort(ara,order=['id','cgpa']))

