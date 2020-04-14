# Problem: What is the probability of throwing one number exactly 3 times 
# on 6 throws of a single die?

import numpy as np

#Number of trials
numtrials = 100000

#Number of successes
success = 0

for i in range(numtrials):
	outcomes = []

	# Generate 6 die throw results
	for roll in range(6): 
		outcome = np.random.randint(1, 7)
		outcomes.append(outcome)

	elements, counts = np.unique(outcomes, return_counts = True)

	if np.count_nonzero(counts == 3) == 1:
		success += 1

	if (i + 1) % 10000 == 0:
		print("{} trials done".format(i + 1))

print(success / numtrials)