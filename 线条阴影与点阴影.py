import numpy as np
from matplotlib.pyplot import *
import matplotlib.transforms as transforms

fig = figure()
ax = fig.add_subplot(121)

t = np.arange(0.,2.5,0.01)
s = np.sin(5*np.pi*t)

line, = ax.plot(t,s,linewidth=5,color='m')


delta = 2/72.
offset = transforms.ScaledTranslation(delta,-delta,fig.dpi_scale_trans)
offset_transform = ax.transData + offset

plot(t,s,linewidth=5,color='gray',transform=offset_transform,zorder=0.9*line.get_zorder())

ax2 = fig.add_subplot(122)
scatter([1,7,3,3,4],[6,0,4,1,2],c='gray')



delta = 2/72.
offset = transforms.ScaledTranslation(-delta,delta,fig.dpi_scale_trans)
offset_transform = ax2.transData + offset

scatter([1,7,3,3,4],[6,0,4,1,2],color='r',transform=offset_transform,zorder=0.5*line.get_zorder())
show()