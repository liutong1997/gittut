import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

# the random data
x = np.random.randn(1000)
y = np.random.randn(1000)

# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005
#参数为（0，1）



# start with a rectangular Figure
plt.figure(figsize=(8, 8))

# plt.axes([left, bottom, width, height]).tick_params(direction='in', top=True, right=True)
# 这句话没影响
ax_histx = plt.axes([left, bottom + width + spacing, height, 0.2])
#自己的理解，要求四个参数，参数过多可以用‘+’连接，长宽交换影响不大，连接的边‘left’与‘bottom’，二者肯定有一个在加法式子里，另一个为单独参数；数字影响比列

# ax_histx.tick_params(direction='in', labelbottom=False)
ax_histy = plt.axes([left + width + spacing, bottom, 0.2, height])
# ax_histy.tick_params(direction='in', labelleft=False)

# the scatter plot:
plt.axes([left, bottom, width, height]).scatter(x, y)

# now determine nice limits by hand:
binwidth = 0.25
lim = np.ceil(np.abs([x, y]).max() / binwidth) * binwidth
# plt.axes([left, bottom, width, height]).set_xlim((-lim, lim))
# plt.axes([left, bottom, width, height]).set_ylim((-lim, lim))

bins = np.arange(-lim, lim + binwidth, binwidth)
ax_histx.hist(x, bins=bins)
ax_histy.hist(y, bins=bins, orientation='horizontal')

# ax_histx.set_xlim(plt.axes([left, bottom, width, height]).get_xlim())
# ax_histy.set_ylim(plt.axes([left, bottom, width, height]).get_ylim())
# 对结果没影响

plt.show()