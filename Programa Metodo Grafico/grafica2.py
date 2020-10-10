import numpy as np
from matplotlib import pyplot as plt

x=np.arange(-6,5.5,0.1)
y=x

plt.axhline(y=5, xmin=0.01, xmax=0.95)
plt.axhline(y=0,xmin=0.01, xmax=0.95)
plt.axvline(x=0, ymin=0.01, ymax=0.95)
plt.fill_between(x,y,5, where= (y <=5), color = 'red')
plt.fill_between(x,y,-10, where= (y <=5), color = 'red')
plt.plot(x,y, 'w')
plt.grid()
plt.show()