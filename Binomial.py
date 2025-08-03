from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np


def calculate_probabilities(start, steps, p, q):

    current = {start: 1.0}
    
    for step in range(steps):
        next_step = defaultdict(float)
        for value, prob in current.items():
            next_step[value + 1] += prob * p  # demo
            next_step[value - 1] += prob * q  # demo
            
        current = next_step
    
    return current

# Parametrs
p = 0.5
q = 1 - p
start_value = 100
#initial_state = {101: p, 99: q}
steps = 150
result = calculate_probabilities(start_value, steps, p, q)
# test 
for key in sorted(result.keys()):
    print(f"${key:.2f}: {result[key]:.4f}")
print(f"\nSum of probabilities: {sum(result.values()):.2f}")

#mean / standart deviation / varience
change = p*(1) + q*(-1)
mean = start_value + steps * abs(change)
print(f"Mean is {mean:.2f}")

#shit for plot
values = sorted(result.keys())
probabilities = [result[v] for v in values]

plt.figure(figsize=(14, 5))
plt.bar(values, probabilities, width=0.8)
plt.axvline(mean, color='red', linestyle='--', label=f'Mean: {mean:.1f}')
plt.ylabel("Probability")
plt.xlabel("Price")
xticks = range(min(values), max(values)+1, 20)
plt.xticks(xticks, rotation=45)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()




