# Problem: What is the probability of throwing one number exactly 3 times 
# on 6 throws of a single die?

import numpy as np

#Number of trials
numtrials = 100000

#Number of successes
success = 0

for i in range(numtrials):
	outcomes = []
	numtrios = 0

	# Generate 6 die throw results
	for roll in range(6): 
		outcome = np.random.randint(1, 7)
		outcomes.append(outcome)

	# Set will have length 4 iff only one number was repeated 3 times. 
	for num in range(6):
		if outcomes.count(num) == 3:
			numtrios += 1

	if numtrios == 1:
		success += 1

	if (i + 1) % 10000 == 0:
		print("{} trials done".format(i + 1))

print(success / numtrials)