import numpy as np
import sys

num_simulations = 100
num_trials = int(5 * 10**6)
num_dice = int(sys.argv[1])
results = []

for _ in range(num_simulations):
	roll_A = 0
	roll_B = 0
	for _ in range(num_dice):
		roll_A += np.random.randint(1, 7, size = num_trials)
		roll_B += np.random.randint(1, 7, size = num_trials)

	ties = roll_A == roll_B
	results.append(np.sum(ties) / num_trials)

print(np.mean(results))