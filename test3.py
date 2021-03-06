#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import matplotlib 


# fc-list :lang=zh-cn
myfont = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/truetype/arphic/ukai.ttc')


x = np.linspace(-1,1,50)
y1 = 2*x-3
y2 = x**2

plt.figure()
plt.plot(x,y1)

plt.figure(3,(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='r',linewidth=1.0,linestyle="--")

plt.xlim((-1,2))
plt.ylim(-2,3)
plt.xlabel('i am x')
plt.ylabel('i am y')

new_ticks = np.linspace(-2,2,7)
plt.xticks(new_ticks)
plt.yticks([-2,-1,0,1,2],\
    [r'$a\ boy$',r'$s\ \alpha$','德',r'$f$',r'$good$'],fontproperties=myfont)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.show()