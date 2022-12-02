win = {
	"Y" : "A",
	"X" : "C",
	"Z" : "B"
}

equal = {
	"X": "A",
	"Y": "B",
	"Z": "C"
}

points = {
	"X": 1,
	"Y": 2,
	"Z": 3
}

with open ("input") as f:
	strat = [x.split(" ") for x in f.read().split("\n")][:-1]

scores = []
for (a,b) in strat:
	score = points[b]
	if win[b] == a: score+=6
	if equal[b]==a: score+=3
	scores+=[score]

#scores = [points[b] + (6 if win[b] == a else 0) + (3 if a==b else 0)  for (a,b) in strat]

print(strat)
print(scores)
print(sum(scores))
