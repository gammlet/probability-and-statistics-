import random
import matplotlib.pyplot as plt
#import numpy as np

path = [1, -1]
steps = 1000
start_value = 100 
values = []
#p = 0.5
#q = 1 - p
#probs = [p, q]

for step in range(steps):
    values.append(start_value)
    
    start_value = start_value + random.choice(path)
    last_val = start_value

time = [i for i in range(len(values))]

eq_x = [0, steps-1]
eq_y = [100, values[-1]]

plt.figure(figsize=(14, 5))

plt.plot(time, values)
plt.plot(eq_x, eq_y, "k--")

plt.ylabel("Value")
plt.xlabel("Time")

plt.show()


