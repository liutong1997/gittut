'''import scipy.misc
import matplotlib.pyplot as plt 

lena = scipy.misc.ascent()
print(lena.shape)
print(lena.max())
print(lena.dtype)


plt.gray()

plt.imshow(lena)
plt.colorbar()
plt.show()'''

import numpy as np 
#a = np.array([1,2,3,4,5,6,7,8])
#d = a.reshape((2,2,2))
#print(d)
from PIL import Image
import matplotlib.pyplot as plt

I = Image.open('test2.png')
print(I.size)
'''arr = np.array(I.getdata(),np.uint8).reshape(1600,1296,4)

plt.imshow(arr)
plt.colorbar()
plt.show()'''
        