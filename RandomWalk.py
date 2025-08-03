import random
import matplotlib.pyplot as plt

paths = [(0, 1), (1, 0), (0, -1), (-1,0)]
U_list = []
V_list = []
n = 1000
x_pos = 0
y_pos = 0

plt.figure()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

for i in range(n):
    path = random.choice(paths)

    U_list.append(path[0])
    V_list.append(path[1])

    # I ahd an scale problem found solution with deepseek
    plt.quiver(x_pos, y_pos, U_list[i], V_list[i], color = "k", angles='xy', scale_units='xy', scale=1, width=0.002, linestyle='--')

    x_pos = x_pos + U_list[i]
    y_pos = y_pos + V_list[i]



plt.grid()
plt.show()





