"""
Problem: Two players play a game. The game starts with S = 0
Player 1 draws random numbers and adds it to S till S > 100, at which point 
Player 1 notes their last number. 
Player 2 continues to add numbers to S till S > 200, at which point Player 
2 notes their last number. 
Player 2 wins if lastNum(Player 2) > lastNum(Player 1) 
Find P(Player 2 wins)
""" 

def q14(seed: int = 37, ntrials: int = 100000) -> float:
	np.random.seed(seed)
	trails_completed = 0
	p2_wins = 0
	while trails_completed < ntrials:
		P1 = 0
		p1_last_num = 0
		p2_last_num = 0
		
		while not P1 > 100:
			rand_num = np.random.randint(1, 101)
			P1 += rand_num
			p1_last_num = rand_num

		# While P2 is still playing
		while not P1 > 200:
			rand_num = np.random.randint(1, 101)
			P1 += rand_num
			p2_last_num = rand_num

		# Condition for player 2 winning
		if p2_last_num > p1_last_num:
			p2_wins += 1

		trails_completed += 1

	return p2_wins / ntrials

print(q14()) # Optional parameters