import matplotlib.pyplot as plt
import numpy as np

# 기본 사용
arr = np.random.standard_normal((30, 40))   # 표준정규분포를 갖는 (30, 40) 형태의 2차원 어레이
# print(arr)
plt.matshow(arr)

plt.show()

# 컬러바 나타내기, shrink 파라미터는 컬러바의 크기, aspect 파라미터는 컬러바의 종횡비
arr = np.random.standard_normal((30, 40))

plt.matshow(arr)
# plt.colorbar()
plt.colorbar(shrink=0.8, aspect=10)

plt.show()

# 색상 범위 지정하기. 범위를 지정하고 해당 범위 밖의 값은 최대 혹은 최소값의 색깔을 가지게 된다.
arr = np.random.standard_normal((30, 40))

plt.matshow(arr)
plt.colorbar(shrink=0.8, aspect=10)
# plt.clim(-1.0, 1.0)
plt.clim(-3.0, 3.0)

plt.show()

# 컬러 맵 설정하기
arr = np.random.standard_normal((30, 40))
# cmap = plt.get_cmap('PiYG')
# cmap = plt.get_cmap('BuGn')
# cmap = plt.get_cmap('Greys')
cmap = plt.get_cmap('bwr')

plt.matshow(arr, cmap=cmap)
plt.colorbar()
plt.show()