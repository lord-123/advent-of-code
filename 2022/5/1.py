with open("input", "r") as f:
	s, m = f.read().split("\n\n")

s = [x[1::4] for x in s.split("\n")]
stacks = {int(x):[] for x in s[-1]}

for x in s[:-1][::-1]:
	for (i, y) in enumerate(x):
		if y != " ":
			stacks[i+1] += [y]

print(stacks)

m = m.split("\n")
moves = [list(map(int, x.split(" ")[1::2])) for x in m][:-1]
print(moves)

for x in moves:
	for i in range(x[0]):
		stacks[x[2]] += stacks[x[1]].pop()

print([x for x in stacks])
print("P1 " + "".join([stacks[x][-1] for x in stacks]))
