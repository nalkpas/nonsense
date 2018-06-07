import numpy as np 
from Collections import defaultdict

# parameters
wr = 0.65
gps_per_quarter = 3
num_byes = 3

gp_pp_payouts = {10:1, 11:2, 12:3, 13:4, 14:4, 15:4}
gp_t8_payouts = {0:0, 1:1, 2:2, 3:4}
pt_pp_payouts = {9:4, 10:6, 11:10, 12:15, 13:15, 14:15, 15:15, 16:15}
pt_t8_payouts = {0:[1,2,3,5], 1:[7,9], 2:[11], 3:[15]}

num_years = 2
num_simulations = 1

gp_finishes = [[],[5],[0,2,3],[3,3]]
pt_finishes = [0,24,6,3]

# simulation
pt_invite = True
rptq_invite = True
# no status = 0, bronze = 1, silver = 2, gold = 3, platinum = 4
status = 4
status_counts_old = np.zeros(5)
status_counts_new = np.zeros(5)
for _ in range(num_simulations):
	for _ in range(num_years):
		status_counts_old[status] += 4
		for quarter in range(4):
			# play the Pro Tour
			if pt_invite:
				pt_invite = False 
				wins = np.random.binomial(16, wr - 0.1)
				pt_pps = pt_pp_payouts.get(wins,3)
				if wins >= 12: 
					pt_pps += np.random.choice(pt_t8_payouts[np.random.binomial(3, wr - 0.1)])
				if wins >= 11:
					pt_invite = True
				pt_finishes[quarter] = pt_pps
			else:
				pt_finishes[quarter] = 0

			# play some GPs
			gp_finishes[quarter] = []
			for _ in range(gps_per_quarter):
				wins = np.random.binomial(15 - num_byes, wr) + num_byes
				gp_pps = gp_pp_payouts.get(wins,0)
				if wins >= 13: 
					gp_pps += gp_t8_payouts[np.random.binomial(3, wr)]
					pt_invite = True
				gp_finishes[quarter] += [gp_pps]

			all_finishes = pt_finishes.copy()
			for finish_set in gp_finishes:
				all_finishes += finish_sets

		pp_count[quarter] += quarter_pps
				



