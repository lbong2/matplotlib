import matplotlib.pyplot as plt
import numpy as np

# 기본 사용1
plt.style.use('default')
plt.rcParams['figure.figsize'] = (6, 5)
plt.rcParams['font.size'] = 12

x = [1, 2, 3]
y = [1, 2, 3]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.bar(x, y, color='aquamarine', edgecolor='black', hatch='/')
ax2.bar(x, y, color='salmon', edgecolor='black', hatch='\\')
ax3.bar(x, y, color='navajowhite', edgecolor='black', hatch='+')
ax4.bar(x, y, color='lightskyblue', edgecolor='black', hatch='*')

plt.tight_layout()
plt.show()

# 기본 사용2
plt.style.use('default')
plt.rcParams['figure.figsize'] = (4, 3)
plt.rcParams['font.size'] = 12

x = [1, 2, 3]
y = [1, 2, 3]

fig, ax = plt.subplots()

bars = ax.bar(x, y, color='lightgray', edgecolor='black')
bars[0].set_hatch('x')
bars[1].set_hatch('O')
bars[2].set_hatch('.')

plt.tight_layout()
plt.show()

# 패턴 밀도 지정하기
plt.style.use('default')
plt.rcParams['figure.figsize'] = (8, 5)
plt.rcParams['font.size'] = 12

x = [1,2,3]
y = [1,2,3]

for i in range(6):
    hatch_str = "/" * i

    ax = plt.subplot(2, 3, i + 1)
    ax.set_title("Hatch String: " + hatch_str)
    bars = ax.bar(x,y,facecolor='skyblue', edgecolor='black')

    for bar in bars:
        bar.set_hatch(hatch_str)

plt.tight_layout()
plt.show()

# 패턴 두께 지정하기
plt.style.use('default')
plt.rcParams['figure.figsize'] = (8, 5)
plt.rcParams['font.size'] = 12
plt.rcParams['hatch.linewidth'] = 3

x = [1,2,3]
y = [1,2,3]

for i in range(6):
    hatch_str = "/" * i

    ax = plt.subplot(2, 3, i + 1)
    ax.set_title("Hatch String: " + hatch_str)
    bars = ax.bar(x,y,facecolor='skyblue', edgecolor='black')

    for bar in bars:
        bar.set_hatch(hatch_str)

plt.tight_layout()
plt.show()