from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
p = 0.25
q = 1 - p
def calculate_probabilities(initial_state, steps):

    current_probs = initial_state.copy()
    
    for step in range(steps):
        next_probs = defaultdict(float)
        
        for value, prob in current_probs.items():
            # These are the possible changes and their probabilities
            # Adjust these according to your specific scenario
            #next_probs[value * 1.01] += prob * p  # real case(have bugs ig)
            #next_probs[value * 0.99] += prob * q  # real case(have bugs ig)
            next_probs[value + 1] += prob * p  # demo
            next_probs[value - 1] += prob * q  # demo
            
        current_probs = dict(next_probs)
    
    return current_probs

# Example usage:
initial_state = {101: p, 99: q}
steps = 25

result = calculate_probabilities(initial_state, steps)

# Print the results sorted by value
for key in sorted(result.keys()):
    print(f"${key:.2f}: {result[key]:.4f}")

# Verify probabilities sum to 1
print(f"\nSum of probabilities: {sum(result.values()):.2f}")

x = np.arange(len(result))
y = result.values()
plt.figure(figsize=(5, 5))
plt.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
plt.ylabel("Probability")
plt.xlabel("Price")
plt.xticks(x, result.keys())
plt.yticks(np.arange(0, 0.2, step=0.015))

plt.show()
