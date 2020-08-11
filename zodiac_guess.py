import random
import numpy as np
from collections import Counter

num_signs = 9
people = list(range(num_signs))
num_simulations = 1000000
results = []
for _ in range(num_simulations):
	guesses = random.sample(people,num_signs)
	matches = sum([a==b for a,b in zip(people, guesses)])
	results.append(matches)

# print(np.mean(results))
result_counts = Counter(results)
max_digits = max([len(str(result)) for result in result_counts.keys()])
for result in sorted(result_counts.keys()):
	print("{result:>{max_digits}}: {frac:.6f} ({count})".format(result=result, 
																frac=result_counts[result]/num_simulations, 
																count=result_counts[result], 
																max_digits=max_digits))