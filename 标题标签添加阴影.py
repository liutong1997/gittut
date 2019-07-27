from matplotlib import patheffects
from matplotlib.pyplot import *
import numpy as np
import matplotlib


matplotlib.rcParams['font.family'] = 'sans-serif'  
matplotlib.rcParams['font.sans-serif'] = ['AR PL UKai CN']

x = np.random.randn(70)
plot(x)

a_title = 'this is a title'
x_label = 'x轴'
y_label = 'this is a ylabel'

title_text_obj = title(a_title,fontsize=18,verticalalignment='baseline',color='red')
title_text_obj.set_path_effects([patheffects.withSimplePatchShadow(offset=(2,-2),shadow_rgbFace='m',alpha=0.8)])

pe = patheffects.withSimplePatchShadow(offset=(2,-2),shadow_rgbFace='m',alpha=0.8)

xlabel_obj = xlabel(x_label)
xlabel_obj.set_path_effects([pe])
ylabel_obj = ylabel(y_label)
ylabel_obj.set_path_effects([pe])
show()