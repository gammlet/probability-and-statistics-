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
p = 0.9
q = 1 - p
start_value = 100 
initial_state = {101: p, 99: q}
steps = 500

#gay ahh shi t 
result = calculate_probabilities(start_value, steps, p, q)

## Print the results sorted by value
#for key in sorted(result.keys()):
#    print(f"${key:.2f}: {result[key]:.4f}")
#
## Verify probabilities sum to 1
#print(f"\nSum of probabilities: {sum(result.values()):.2f}")

#mean / standart deviation / varience
change = p*(1) + q*(-1)
mean = start_value + steps * abs(change)
print(f"Mean is {mean:.2f}")

values = sorted(result.keys())
probabilities = [result[v] for v in values]

x = np.arange(len(result))
y = result.values()

plt.figure(figsize=(14, 5))
#plt.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
bars = plt.bar(values, probabilities, width=0.8)

plt.axvline(mean, color='red', linestyle='--', label=f'Theoretical Mean: {mean:.1f}')
plt.ylabel("Probability")
plt.xlabel("Price")

xticks = range(min(values), max(values)+1, 20)
plt.xticks(xticks, rotation=45)



plt.show()




