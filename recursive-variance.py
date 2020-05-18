#Variance of recursive function
# Problem: Given the recursive function defined below, find its variance. 

import numpy as np 

results = np.empty(100000)

def recurse():
	x = np.random.choice([1,2,3])   # equally likely values 1,2,3
	if(x == 1): return 3
	elif(x == 2): return(5 + recurse())
	else: return(7 + recurse())

for i in range(100000):
	results[i] = recurse()

print(np.var(results))