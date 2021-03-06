import numpy as np
from matplotlib import pyplot as plt

x=np.arange(-2,2,0.1)
y=-2*x + 3
z= x

plt.plot(x,y,'m')
plt.plot(x,z,'r')
plt.axhline(y=1/2, xmin=0.01, xmax=0.95)
plt.axhline(y=0, xmin=0.01, xmax=0.95)
plt.axvline(x=0, ymin=0.01, ymax=0.95)
plt.fill_between(x,z,7, where=(z>1), color='red')
plt.fill_between(x,y,7,where=(z<1.1), color='red')
plt.grid()
plt.show()