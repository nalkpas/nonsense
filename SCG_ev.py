import numpy as np
import scipy.stats as sps

print('Team SCG')
win_rates = [0.6, 0.65, 0.7]
prizes = {10: 100, 11: 200, 12:300, 13: 500, 14: 1000, 15: 2500}
for win_rate in win_rates:
  total = 0
  for wins in range(10,16):
    top8_ev = np.sum([sps.binom.pmf(top8_wins, 3, win_rate) * prizes[top8_wins + 12] for top8_wins in range(4)])
    if wins < 12:
      total += sps.binom.pmf(wins, 15, win_rate) * prizes[wins]
    if wins >= 12:
      total += sps.binom.pmf(wins, 15, win_rate) * top8_ev
  print('{:<5}: {}'.format(win_rate, total))

print('\nSCG')
prizes = {9: 100, 10: 200, 11: 325, 12: 500, 13: 1000, 14: 2000, 15: 5000}
for win_rate in win_rates:
  total = 0
  for wins in range(9,16):
    top8_ev = np.sum([sps.binom.pmf(top8_wins, 3, win_rate) * prizes[top8_wins + 12] for top8_wins in range(4)])
    if wins < 12:
      total += sps.binom.pmf(wins, 15, win_rate) * prizes[wins]
    if wins >= 12:
      total += sps.binom.pmf(wins, 15, win_rate) * top8_ev
  print('{:<5}: {}'.format(win_rate, total))

byes = 3
print('\n35k GP ({} byes)'.format(byes))
prizes = {11: 300, 12: 434, 13: 750, 14: 1500, 15: 3000, 16: 6000}
for win_rate in win_rates:
  total = 0
  for wins in range(11,16):
    top8_ev = np.sum([sps.binom.pmf(top8_wins, 3, win_rate) * prizes[top8_wins + 13] for top8_wins in range(4)])
    if wins < 13:
      total += sps.binom.pmf(wins - byes, 15 - byes, win_rate) * prizes[wins]
    if wins >= 13:
      total += sps.binom.pmf(wins - byes, 15 - byes, win_rate) * top8_ev
  print('{:<5}: {}'.format(win_rate, total))
