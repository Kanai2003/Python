import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
def s(flip = 2):
    x = np.linspace(0,14,100)
    for i in range(1,5):
        plt.plot(x,np.sin(x+i*.5)*(7-i)*flip)

sb.set()
s()
plt.show()