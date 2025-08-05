import random
import matplotlib.pyplot as plt
import numpy as np

path = [1, -1]
steps = 1000
start_value = 100 
values = []
p = 0.8
q = 1 - p
probs = [p, q]

for step in range(steps):
    values.append(start_value)
    start_value = start_value + random.choices(path, weights=probs, k=1)[0]
    last_val = start_value

time = [i for i in range(len(values))]
spaced_eq_x =  np.linspace(0, steps - 1, len(values)) 
spaced_eq_y =  np.linspace(100, values[-1], len(values)) 

def calc_diff():
    diff_list =np.array(values) - np.array(spaced_eq_y)
    return diff_list 

def show_plot(diff_list):
    plt.figure(figsize=(14, 5))
    plt.subplot(2, 1 ,1)
    plt.plot(time, values, label = "Stock")
    plt.plot(spaced_eq_x, spaced_eq_y, "k--", label = "Linear Trend")
    plt.legend()
    plt.grid()
    plt.subplot(2, 1 ,2)
    plt.plot(time, diff_list, "--", label = " Difference")
    plt.ylabel("Value")
    plt.xlabel("Time")
    plt.legend()
    plt.grid()
    plt.show()

print(calc_diff())
show_plot(calc_diff())

