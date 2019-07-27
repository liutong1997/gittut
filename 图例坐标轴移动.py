import matplotlib.pyplot as plt
import numpy as np
x1 = np.linspace(-np.pi,np.pi,256)
y1 = np.sin(x1)
y2 = np.cos(x1)

plt.figure()
o1, = plt.plot(x1,y1,label='sin',linestyle='steps')
o2, = plt.plot(x1,y2,c='yellow',label='cos',linestyle='--')
plt.axhline(0.5,-2,2,c='red',label='straight_line',linestyle=':')
plt.legend(handles=[o1,o2,],loc='best')


plt.title('The figure of $\sin$ and $\cos$')
plt.ylim(-1.2,1.2)
plt.xlim(-3,3)
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],\
    [r'$-\pi$',r'$-\pi/2,0$',r'$0$',r'$\pi/2$',r'$\pi$'])


plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data',0))
plt.gca().spines['left'].set_position(('data',0))


plt.show()
