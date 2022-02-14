import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4])
plt.show()

# x, y값 매칭 가능
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

# 스타일 지정하기. ro = red + circle('o') marker
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

# 200ms 간격으로 균일하게 샘플된 시간
t = np.arange(0., 5., 0.2)

# 빨간 대쉬, 파란 사각형, 녹색 삼각형
# 순서대로 f(t) = t, f(t) = t^2, f(t) = t^3
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()