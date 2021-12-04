boards = []
with open("input", "r") as file:
	numbers = [int(x) for x in file.readline().split(",")]

	i = 0
	line = file.readline()
	while line:
		boards += [[[(int(x), False) for x in file.readline().split()] for i in range(5)]]
		line = file.readline()

"""
for b in boards:
	for l in b:
		print(l)
	print("")
	"""

winners = []
bingo = False
for i in numbers:
	if bingo:
		break
	for j,b in enumerate(boards):
		boards[j] = [[(x[0], x[0]==i or x[1])for x in line] for line in b]
	for j,b in enumerate(boards):
		if sum([sum(x[1] for x in l)==5 for l in b]) or sum([sum(x[k][1] for x in b)==5 for k in range(5)]):
			if j not in winners: winners += [j]
			if len(winners) == len(boards):
				unmarked = sum(sum(x[0] for x in l if not x[1]) for l in b)
				print(unmarked, i, unmarked* i)
				bingo = True
				break
