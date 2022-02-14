import matplotlib.pyplot as plt
import numpy as np

# 기본 사용, y방향의 에러바를 출력한다.
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
yerr = [2.3, 3.1, 1.7, 2.5]

plt.errorbar(x, y, yerr=yerr)
plt.show()

# 비대칭 편차 나타내기, 이때 yerr는 위와 다르게 위 아래 범위를 나타낸다.
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
yerr = [(2.3, 3.1, 1.7, 2.5), (1.1, 2.5, 0.9, 3.9)]

plt.errorbar(x, y, yerr=yerr)
plt.show()

# 상한 하한 기호 표시하기, 위아래 화살표를 통해 상한 하한이 표시된다.
x = np.arange(1, 5)
y = x**2
yerr = np.linspace(0.1, 0.4, 4)     # 0.1, 0.2, 0.3, 0.4
print(yerr)
plt.errorbar(x, y + 4, yerr=yerr)
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, lolims=True)

upperlimits = [True, False, True, False]
lowerlimits = [False, False, True, True]
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits)
plt.show()