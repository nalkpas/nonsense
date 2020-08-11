import random

from collections import Counter

# generate deck and declare variables
num_iterations = 1000000
# p_anthem = 0.1429
p_anthem = 0.25
decklist = {'Explosion': 4, 'land': 22, 'Spiral': 4, 'brick': 16}
deck = []
for card in decklist.keys():
  deck += [card] * decklist[card]

# simulation loop
count_six = 0
count_nine = 0
for _ in range(num_iterations):
  draw = random.sample(deck, 3)
  if 'Explosion' in draw[:2]:
    count_six += 1
    count_nine += (1 - p_anthem)
  elif 'land' in draw[:2] and 'Explosion' == draw[2]:
    count_nine += (1 - p_anthem)
  elif 'Spiral' == draw[0] and 'Explosion' == draw[2]:
    count_six += (1 - p_anthem)

# print results
print('6/6 wins:\t' + str(round(count_six / num_iterations,4)))
print('9/9 wins: \t' + str(round(count_nine / num_iterations,4)))
