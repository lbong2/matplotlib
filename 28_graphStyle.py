import matplotlib.pyplot as plt

# 기본 사용, 미리 만들어져 있는 그래프 스타일 사용가능.
plt.style.use('bmh')
# plt.style.use('ggplot')
# plt.style.use('classic')
# plt.style.use('Solarize_Light2')
# plt.style.use('default')

plt.plot([1, 2, 3, 4], [4, 6, 2, 7])
plt.show()

# 사용할 수 있는 스타일 목록
print(plt.style.available)

# rcParams 사용하기1, 각각의 스타일 관련 파라미터를 지정할 수 있다.
plt.style.use('default')
plt.rcParams['figure.figsize'] = (6, 3)
plt.rcParams['font.size'] = 12
# plt.rcParams['figure.figsize'] = (4, 3)
# plt.rcParams['font.size'] = 14

plt.plot([1, 2, 3, 4], [4, 6, 2, 7])
plt.show()

# rcParams 사용하기2
plt.style.use('default')
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['lines.linestyle'] = '-'
# plt.rcParams['lines.linewidth'] = 5
# plt.rcParams['lines.linestyle'] = '--'

plt.plot([1, 2, 3, 4], [4, 6, 2, 7])
plt.show()

# rcParams 사용하기3