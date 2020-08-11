from collections import Counter
import random

# generate deck and declare variables
num_iterations = 100000
cards_seen = 10
CCDD_count = 1
decklist = {'C': 9, 'D': 8, 'X': 0, 'CCDD': CCDD_count, 'S': 23 - CCDD_count}
# deck = {'X': 6, 'Y': 7, 'D': 4, 'O': 23}
deck = []
for card in decklist.keys():
	deck += [card] * decklist[card]

# simulation loop
count = 0
count_four_plus = 0
count_CCDD = 0
for _ in range(num_iterations):
	draw = Counter(random.sample(deck, cards_seen))
	count += (min(draw['C'], 2) + min(draw['D'], 2) + draw['X'] >= 4) and (draw['CCDD'] > 0)
	count_four_plus += (draw['C'] + draw['D'] + draw['X'] >= 4) and (draw['CCDD'] > 0)
	count_CCDD += (draw['CCDD'] > 0)

# print results	
for card, number in decklist.items():
	print(card + ': ' + str(number) + '\t', end='')
print()
print('fraction of draws with CCDD:\t' + str(round(count / count_CCDD,3)))
print('4 or more lands:            \t' + str(round(count_four_plus / count_CCDD,3)))
print('CCDD given 4 or more lands: \t' + str(round(count / count_four_plus,3)))