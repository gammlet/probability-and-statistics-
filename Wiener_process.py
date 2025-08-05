import random
import matplotlib.pyplot as plt
import numpy as np

path = [1, -1]
steps = 10
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


spaced_eq_x =  np.linspace(0, steps - 1, len(values)) 
spaced_eq_y =  np.linspace(100, values[-1], len(values)) 


def calc_diff():
    diff_list = []
    for i in range(len(spaced_eq_y)):
        difference = spaced_eq_y[i] - values[i]
        diff_list.append(difference)
    return diff_list 

def show_plot():
    plt.figure(figsize=(14, 5))
    plt.plot(time, values)
    plt.plot(spaced_eq_x, spaced_eq_y, "k--")
    plt.ylabel("Value")
    plt.xlabel("Time")
    plt.show()

print(calc_diff())
show_plot()

