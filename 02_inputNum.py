import matplotlib.pyplot as plt
import numpy as np

plt.plot([2, 3, 5, 10])
# plt.plot(np.array([2,3,5,10])) 이거도 가능
plt.show()

# 순서대로 (1, 2)(2, 3)(3, 5)(4, 10) 좌표 지나는 꺾은선 그래프 나타남
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.show()

# Label 있는 데이터 사용하기.
data_dict = {'data_x': [1, 2, 3, 4, 5], 'data_y': [2, 3, 5, 10, 8]}

plt.plot('data_x', 'data_y', data=data_dict)
plt.show()