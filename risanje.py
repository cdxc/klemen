import matplotlib.pyplot as plt
from numpy import *
plt.style.use(['dark_background'])


#async def graph(ctx, arg):
def risanje(function, xmin, xmax, ymin, ymax):
    x = linspace(xmin-1,xmax+1, 222)
    y = eval(function)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['left'].set_color('grey')
    ax.spines['bottom'].set_color('grey')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    plt.plot(x,y, 'c')
    plt.savefig("fig", bbox_inches='tight')
    #plt.show()
