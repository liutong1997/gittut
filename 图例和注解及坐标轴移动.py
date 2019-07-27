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

# import numpy as np 
# #a = np.array([1,2,3,4,5,6,7,8])
# #d = a.reshape((2,2,2))
# #print(d)
# from PIL import Image
# import matplotlib.pyplot as plt

# I = Image.open('test2.png')
# print(I.size)
'''arr = np.array(I.getdata(),np.uint8).reshape(1600,1296,4)

plt.imshow(arr)
plt.colorbar()
plt.show()'''


from matplotlib.pyplot import *
import numpy as np
import matplotlib

matplotlib.rcParams['font.family'] = 'sans-serif'  
matplotlib.rcParams['font.sans-serif'] = ['AR PL UKai CN']

x = [x for x in range(-100,100)]
y = [((x)**2-2000) for x in range(-100,100)]
new_xtic = [n for n in range(-100,101,40)]


index = -1
action = False
for value in new_xtic:
    if value == 0:
        index+=1
        break
    elif value > 0:
        action = True
        index+=1
        break
    else:
        index+=1

if action:
    zh_xtic = new_xtic[0:index]+['原点']+new_xtic[index:-1]
    new_xtic = new_xtic[0:index]+[0]+new_xtic[index:-1]
else:
    zh_xtic = new_xtic[:]
    zh_xtic[index] = '原点'


xticks(new_xtic,zh_xtic)
plot(x,y,label='line')

x1 = np.random.normal(500,100,100)
x2 = np.random.normal(1000,100,100)
plot(x1,label='normal line1')
plot(x2,label='normal line2')



legend(loc='best',ncol=3)
# best
# upper right
# upper left
# lower left
# lower right
# right
# center left
# center right
# lower center
# upper center
# center
annotate("the 1000's normal line",(25,1000),xytext = (10,2000),arrowprops = dict(arrowstyle='->'))

gca().spines['right'].set_color('none')
gca().spines['top'].set_color('none')
gca().spines['bottom'].set_position(('data',0))
gca().spines['left'].set_position(('data',0))

show()