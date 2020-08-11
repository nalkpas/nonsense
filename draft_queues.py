import numpy as np

win_rates = np.arange(0.1,1,0.1)
num_simulations = 250000

means = []
std_devs = []
for win_rate in win_rates:
	sim_wins = []
	total_losses = 0
	for _ in range(num_simulations):
		wins = 0
		match_result = 1
		while wins <= 3 and match_result == 1:
			match_result = np.random.choice(2, p=[1 - win_rate, win_rate])
			if match_result == 1:
				wins += 1
		sim_wins.append(wins)
		if match_result == 0:
			total_losses += 1
	sim_mean = np.sum(sim_wins) / (np.sum(sim_wins) + total_losses)
	means.append(sim_mean)
	std_devs.append(np.std(sim_wins))

for win_rate in win_rates:
	print('{0:.2f}, '.format(float(win_rate)), end='')
print()
for mean in means:
	print('{0:.2f}, '.format(mean), end='')
print('\n')
for win_rate in win_rates:
	print('{0:.2f}, '.format(float((3*win_rate*(1 - win_rate))**0.5)), end='')
print()
for std_dev in std_devs:
	print('{0:.2f}, '.format(std_dev), end='')
print()