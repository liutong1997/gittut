
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-np.pi,np.pi,256)
y1 = np.sin(x1)
y2 = np.cos(x1)
y3 = 1.5+0*x1

left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005

plt.figure()



plt.axes([left, bottom + width + spacing, height, 0.2]).plot(x1,y2,c='yellow',label='cos',linestyle='--',marker='>')
plt.axes([left + width + spacing, bottom, 0.2, height]).plot(x1,y3,label='straightline')
plt.axes([left, bottom, width, height]).plot(x1,y1,label='sin',linestyle='steps',marker='p')
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],\
    [r'$-\pi$',r'$-\pi/2,0$',r'$0$',r'$\pi/2$',r'$\pi$'])
plt.show()