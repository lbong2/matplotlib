import matplotlib.pyplot as plt
import numpy as np

# x축 scale 정하기, symlog = Symmetrical Log Scale
x = np.linspace(-10, 10, 100)
y = x ** 3

plt.plot(x, y)
plt.xscale('symlog')

plt.show()

# y축 scale 정하기,
x = np.linspace(0, 5, 100)
y = np.exp(x)

plt.plot(x, y)
# plt.yscale('linear')
plt.yscale('log')

plt.show()