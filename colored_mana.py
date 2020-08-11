import random

lands = 6*['B'] + 6*['U'] + 6*['G']
# lands = 4*['B'] + 3*['U'] + 3*['G'] + 3*['W'] + 3*['UG'] + 1*['UW'] + 1*['WB']
num_simulations = 500000

lands_drawn = [3, 4, 5, 6]
for num_lands in lands_drawn:
    counts = [0] * 5
    for _ in range(num_simulations):
        lands_drawn = random.sample(lands, num_lands)
        colors = []
        for card in lands_drawn: 
            colors += list(card)
        colors = set(colors)
        counts[len(colors)] += 1
    print('{}: {}'.format(num_lands, [count / num_simulations for count in counts]))