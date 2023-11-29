# numpy examples
# single dimensional array
'''import numpy as np
arr = np.array([1,2,3,4])
print(arr)
## multi dimensional array
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1)
##intialization numpy arrays with zeros
arr3 = np.zeros([2,2])
print(arr3)
## intialization numpy arrays with full
arr4 = np.full((4,4),5)
print(arr4)
## intialization numpy arrays with a range
arr5 = np.arange(1,51)
print(arr5)
## intialization numpy arrays with a range including step
arr6 = np.arange(5,51,5)
print(arr6)
## intialization numpy arrays with randomization
arr7 = np.random.randint(1,50,5)
print(arr7)
## change the shape of numpys
arr8 = np.array([[1,2,3],[4,5,6]])
print(arr8)
print(arr8.shape)
arr8.shape = (3,2)
print(arr8)
## joining numpy arrays with vstack
n1 = np.array([10,20,30])
n2 = np.array([40,50,60])
x = np.vstack((n1,n2))
print(x)
# ## joining numpy arrays with hstack
n1 = np.array([10,20,30])
n2 = np.array([40,50,60])
y = np.hstack((n1,n2))
print(y)
## joining numpy arrays with column_stack
n1 = np.array([10,20,30])
n2 = np.array([40,50,60])
z = np.column_stack((n1,n2))
print(z)
## numpy intersections
n1 = np.array([10,20,30,40,50,60])
n2 = np.array([50,60,70,80,90])
s = np.intersect1d(n1,n2)
print(s)
## numpy differences
n1 = np.array([10,20,30,40,50,60])
n2 = np.array([50,60,70,80,90])
d = np.setdiff1d(n1,n2)
c = np.setdiff1d(n2,n1)
print(d)
print(c)

import  numpy as np
n1 = np.array([10,20,30,40])
n2 = np.array([20,30,40,50])
n3 = np.array([10,20,30,40])
n3 = n3 * 5
n3 = np.std(n3)
n2 = n2 - 1
n2 = np.median(n2)
n1 = n1+1
n1 = np.mean(n1)
print(n1)
print(n2)
print(n3)'''
## save and loading numpy arrays
import numpy as np
n1 = np.array([10,20,30,40,50,60,70])
n1 = np.save('final_numpy_array',n1)
n2 = np.load('final_numpy_array.npy')
print(n2)


