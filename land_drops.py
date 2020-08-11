from collections import Counter
import random
import numpy as np

deck = {'L': 25,'S': 35}
# deck = {'L': 17,'S': 23}
decklist = []
for card in deck.keys():
	decklist += [card] * deck[card]

def is_mulligan(hand):
	counts = Counter(hand)
	size = len(hand)
	if size == 7 and (counts['L'] >= (size - 1) or counts['L'] <= 1):
		return True
	elif size < 7 and (counts['L'] == 0 or counts == size):
		return True
	return False

num_simulations = 1000000
on_play = True
turns = 6
counter = np.zeros(turns)
total_mulligans = 0
for _ in range(num_simulations):
	draw = random.sample(decklist, 7 + turns + (not on_play))
	mulligans = 0
	while is_mulligan(draw[:7 - mulligans]) and mulligans <= 7:
		mulligans += 1
		draw = random.sample(decklist, 7 + turns + (not on_play) - mulligans + 1)
	total_mulligans += mulligans
	for turn in range(1,turns + 1):
		counts = Counter(draw[:7 - mulligans + turn + (not on_play) + (mulligans > 0)])
		if counts['L'] >= turn:
			counter[turn - 1] += 1

probs = counter / num_simulations
if on_play:
	print("on play")
else:
	print("not on play")
for turn in range(1,turns + 1):
	print(str(turn) + '\t', end='')
print('')
for prob in probs:
	print(str(round(prob,3)) + '\t', end='')
print('')
print('avg mulligans: ' + str(total_mulligans / num_simulations))