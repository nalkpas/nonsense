import numpy as np

num_episodes = 5
num_trials = int(2.5 * 10**6)
num_dice = 5

for _ in range(num_episodes):
	roll_A = 0
	roll_B = 0
	for _ in range(num_dice):
		roll_A += np.random.randint(1, 6, size = num_trials)
		roll_B += np.random.randint(1, 6, size = num_trials)

	ties = roll_A == roll_B
	print(np.sum(ties) / num_trials)