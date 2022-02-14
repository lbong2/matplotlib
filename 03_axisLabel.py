import matplotlib.pyplot as plt

# xlabel, ylabel로 라벨 이름 설정 가능. plot에 표시됨.
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.show()

# 여백 지정 가능.
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', labelpad=5)
plt.ylabel('Y-Axis', labelpad=10)
plt.show()

# 폰트 설정 가능. 차례로 글꼴, 색깔, 굵기, 사이즈// 사이즈는 숫자 혹은 속성 사용 가능.
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', labelpad=5, fontdict={'family': 'serif', 'color': 'b', 'weight': 'bold', 'size': 14})
plt.ylabel('Y-Axis', labelpad=10, fontdict={'family': 'fantasy', 'color': 'deeppink', 'weight': 'normal', 'size': 'xx-large'})
plt.show()

# 이렇게 폰트 dictionary 만들어서 사용 가능.
font1 = {'family': 'serif',
         'color': 'b',
         'weight': 'bold',
         'size': 14
         }

font2 = {'family': 'fantasy',
         'color': 'deeppink',
         'weight': 'normal',
         'size': 'xx-large'
         }

plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', labelpad=5, fontdict=font1)
plt.ylabel('Y-Axis', labelpad=10, fontdict=font2)
plt.show()

# 위치 지정. loc속성을 사용해 라벨 위치 변경 가능. {‘left’, ‘center’, ‘right’}, {‘bottom’, ‘center’, ‘top’}
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', loc='right')
plt.ylabel('Y-Axis', loc='top')
plt.show()