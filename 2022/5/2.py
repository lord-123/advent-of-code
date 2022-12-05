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

print(stacks)
print("moving")
for x in moves:
	stacks[x[2]] += stacks[x[1]][-x[0]:]
	del stacks[x[1]][-x[0]:]
	print(x)
	print(stacks)

print(stacks)
print("stacks " + "".join([stacks[x][-1] for x in stacks]))
