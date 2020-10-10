import numpy as np
from matplotlib import pyplot as plt

x=np.arange(-5,5,0.1)
y=(1/2)*x+1

plt.axhline(y=0, xmin=0.01, xmax= 0.95)
plt.axvline(x=0, ymin=0.01, ymax= 0.95)
plt.plot(x,y,'m')
plt.fill_between(x, y, 6, color='blue')
plt.grid()
plt.show()