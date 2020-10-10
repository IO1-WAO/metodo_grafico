import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-10, 10, 0.1)
y = -2*x + 5

plt.plot(x,y, 'm')
plt.axhline(y=0, xmin=0.01, xmax= 0.95)
plt.axvline(x=0, ymin=0.01, ymax= 0.95)
plt.fill_between(x, y, -15, color='blue')
plt.grid()
plt.show()