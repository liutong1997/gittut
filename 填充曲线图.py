import matplotlib
from matplotlib.pyplot import *
import numpy as np


x = np.arange(0.0,3.5,0.01)
y1 = np.sin(2*np.pi*x)
y2 = 1.2*np.cos(2*np.pi*x)

plot(x,y1,x,y2,c='r')
fill_between(x,y1,y2,where = y2>y1,facecolor='darkblue',interpolate = True)
fill_between(x,y1,y2,where = y1>y2,facecolor='deeppink',interpolate = True)

show()