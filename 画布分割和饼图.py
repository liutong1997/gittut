#coding=utf-8
from matplotlib.pyplot import *
import matplotlib.font_manager 
import numpy as np

matplotlib.rcParams['font.family'] = 'sans-serif'  
matplotlib.rcParams['font.sans-serif'] = ['AR PL UKai CN']
font = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/truetype/arphic/ukai.ttc')

fig = figure(figsize=(8,8))
# ax1 = Axes(fig,[0.1,0.1,0.4,0.4])
ax1 = axes([0.1,0.1,0.4,0.4])
fig.add_axes(ax1)


ax2 = Axes(fig,[0.4,0.4,0.4,0.4])
fig.add_axes(ax2)



labels = '春天','Summer','Fall','Winter'
x=[15,30,45,10]
fig.suptitle('我是最大的标题',fontproperties=font,fontsize=25)


ax1.pie(x,labels=labels,autopct='%.1f%%',startangle=66,explode=(0.1,0.1,0.1,0.1))
ax1.set_title('Rainy days by seasons')
ax2.pie(x,labels=labels,autopct='%.1f%%',startangle=90)
ax2.set_title('Rainy days by seasons')

show()