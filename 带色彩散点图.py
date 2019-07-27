from matplotlib.pyplot import *
import matplotlib.font_manager 
import numpy as np


matplotlib.rcParams['font.family'] = 'sans-serif'  
matplotlib.rcParams['font.sans-serif'] = ['AR PL UKai CN']


x = np.random.randn(1000)
y1 = np.random.randn(len(x))
y2 = 1.2+np.exp(x)

subplot(121)
scatter(x,y1,c='indigo',alpha=0.3,edgecolors='white',marker='*',label='正态分布散点')
legend(loc='best')
xlabel('正态分布散点')


subplot(122)
scatter(x,y2,c='green',alpha=0.3,edgecolors='gray',marker='4',label='正态分布e次方的幂')
legend(loc='best')
xlabel('正态分布e次方的幂')

show()