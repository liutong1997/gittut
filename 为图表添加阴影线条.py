import numpy as np
from matplotlib.pyplot import *
import matplotlib.transforms as transforms


def setup(layout=None):
    assert layout is not None


    fig = figure()
    ax = fig.add_subplot(layout)
    return fig,ax


def get_singal():
    t = np.arange(0.,2.5,0.01)
    s = np.sin(5*np.pi*t)
    return t,s


def plot_singal(t,s):
    line, = axes.plot(t,s,linewidth=5,color='m')
    return line,


def make_shdow(fig,ax,line,t,s):
    delta = 2/72.
    offset = transforms.ScaledTranslation(delta,-delta,fig.dpi_scale_trans)
    offset_transform = axes.transData + offset

    axes.plot(t,s,linewidth=5,color='gray',transform=offset_transform,zorder=0.5*line.get_zorder())

if __name__ == '__main__':
    fig,axes = setup(111)
    t,s = get_singal()
    line, = plot_singal(t,s)

    make_shdow(fig,axes,line,t,s)

    axes.set_title('shadow')
    show()