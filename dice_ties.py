import numpy as np
import sys

num_simulations = 5
num_trials = int(8 * 10**6)
num_dice = int(sys.argv[1])

for _ in range(num_simulations):
	roll_A = 0
	roll_B = 0
	for _ in range(num_dice):
		roll_A += np.random.randint(1, 7, size = num_trials)
		roll_B += np.random.randint(1, 7, size = num_trials)

	ties = roll_A == roll_B
	print(np.sum(ties) / num_trials)