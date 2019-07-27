from matplotlib.pyplot import *
import numpy as np


x = np.arange(0,10,1)

y = np.log(x)
#误差
xe = 0.1*np.abs(np.random.randn(len(y)))

bar(x,y,yerr = xe,width = 0.4,align = 'center',edgecolor = 'm',hatch =r'.',color = 'cyan')
# gca().spines['right'].set_color('none')
# gca().spines['top'].set_color('none')
# gca().spines['bottom'].set_position(('data',0))
# gca().spines['left'].set_position(('data',0))
# gca().xaxis.set_ticks_position('bottom')
# gca().yaxis.set_ticks_position('left')

show()