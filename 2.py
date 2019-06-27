import numpy as np


array = np.array([[1,2,3],\
                  [2,3,4]],dtype = np.int64)
#print('{}\nnumber of element:{}\n{}\n{}'.format(array.dtype,array.size,array.shape,array.ndim))
#print(np.arange(1,2,0.1).reshape(2,5))
#print(np.linspace(1,20,5))
b = np.array([2,2,4,5]).reshape(2,2)
a = np.array([2,3,7,5]).reshape(2,2)
#print(a*b)
#print(np.dot(a,b),end='\t')
#print(np.max(a.dot(b),axis=0))
c = np.array([1,3,4,2]).reshape(2,2)
d = np.sum(c,axis=0)
print('{}\t{}'.format(c,d))