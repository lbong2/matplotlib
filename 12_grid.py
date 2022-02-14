import matplotlib.pyplot as plt
import numpy as np

# 기본 사용, grid(True) -> x, y축에 대해 그리드가 생성됨.
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='springgreen', marker='^', markersize=9)
plt.grid(True)

plt.show()

# 축 지정하기, axis 파라미터를 지정함으로 축 지정 가능. y로 설정하면 가로줄만 남음.
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='forestgreen', marker='^', markersize=9)
plt.grid(True, axis='y')

plt.show()

# 스타일 설정하기, 파라미터
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='springgreen', marker='^', markersize=9)
plt.grid(True, axis='y', color='red', alpha=0.5, linestyle='--')

plt.show()