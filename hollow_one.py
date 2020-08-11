import numpy as np
import scipy.stats as sps

bois_in_hand = 1
on_play = False
p_outcomes = np.zeros(5)

for bois_after_drawing in range(bois_in_hand, 5):
	p_bois_after_drawing = sps.hypergeom.pmf(bois_after_drawing - bois_in_hand, 52 + on_play, 4 - bois_in_hand, 3)
	p_bois_after_discarding = np.array([sps.hypergeom.pmf(i, 9 - on_play, bois_after_drawing, 6 - on_play) for i in range(5)])
	p_outcomes += p_bois_after_discarding * p_bois_after_drawing

if on_play:
	print('on play')
else:
	print('on draw')
for p in p_outcomes[:-1]:
	print('{0:.6f}'.format(p), end=', ')
print('{0:.6f}'.format(p_outcomes[-1]))
print('probability of casting at least 1 Hollow One: {}'.format(1 - p_outcomes[0]))
print('expected Hollow Ones: {}'.format(np.sum([n*p_n for n, p_n in zip(range(5), p_outcomes)])))
