import numpy as np 
import csv
import pdb

names = []
file_read = []
with open('poll_responses.csv', 'r') as file:
	reader = csv.reader(file)
	for line in reader:
		names.append(line[1])
		file_read.append(line[2:])

names = names[1:]
card_names = file_read[0]
scores = file_read[1:]

card_names = [name.strip().strip('[').strip(']').replace(' ', '_').replace(',','') for name in card_names]
scores = np.array(scores, dtype = float)

rating_means = np.mean(scores, axis=0)
user_means = np.mean(scores, axis=1).reshape(-1,1)
user_stds = np.std(scores, axis=1).reshape(-1,1)

norm_scores = (scores - user_means) / user_stds
norm_rating_means = np.mean(norm_scores, axis = 0)

with open('poll_responses_reformatted.csv', 'w') as file:
	file.write('card_name,')
	for name in names[:-1]:
		file.write(str(name) + ',')
	file.write(str(names[-1]) + ',')
	file.write('mean,norm_mean\n')

	scores_t = scores.T 
	for i in range(len(scores_t)):
		file.write(str(card_names[i]) + ',')
		for rating in scores_t[i][:-1]:
			file.write(str(rating) + ',')
		file.write(str(scores_t[i][-1]) + ',')
		file.write(str(rating_means[i]) + ',' + str(norm_rating_means[i]) + '\n')

print('done')