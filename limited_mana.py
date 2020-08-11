from collections import Counter
import random

# generate deck and declare variables
num_iterations = 200000
cards_seen = 7
# decklist = {'C': 9, 'D': 8, 'X': 0, 'S': 23}
decklist = {'C': 8, 'D': 5, 'X': 12, 'S': 35}

deck = []
for card in decklist.keys():
	deck += [card] * decklist[card]

# simulation loop
count = 0
for _ in range(num_iterations):
	draw = Counter(random.sample(deck, cards_seen))
	count += (min(draw['C'], 1) + min(draw['D'], 1) + draw['X'] >= 2)

# print results	
for card, number in decklist.items():
	print(card + ': ' + str(number) + '\t', end='')
print()
print('fraction of draws with both colors:\t' + str(round(count / num_iterations,3)))