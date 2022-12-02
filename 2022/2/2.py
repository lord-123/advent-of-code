with open ("input") as f:
	strat = [x.split(" ") for x in f.read().split("\n")][:-1]

scores = []
for (a,b) in strat:
	score = 0
	if b == "X":
		score += (ord(a)-63)%3+1
	elif b == "Y":
		score += 3
		score += ord(a)-64
	elif b == "Z":
		score += 6
		score += (ord(a)-64)%3+1
	scores += [score]

print(sum(scores))
