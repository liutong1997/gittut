from matplotlib.pyplot import *
import numpy as np
import matplotlib

matplotlib.rcParams['font.family'] = 'sans-serif'  
matplotlib.rcParams['font.sans-serif'] = ['AR PL UKai CN']

x = np.arange(-2,2,0.01)
y = np.sinc(2*np.pi*x)
plot(x,y)

col_labels = ['col1','col2','col3']
row_labels = ['row1','row2','row3']
table_vals = [[11,12,13],[21,22,23],[28,29,30]]
row_colors = ['red','gold','green']
my_table = table(cellText=table_vals, colWidths=[0.1]*4,\
   rowLabels=row_labels, colLabels=col_labels,\
   rowColours=row_colors, colColours=row_colors,\
   loc='center right')

show()