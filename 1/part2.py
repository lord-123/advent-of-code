with open("input", "r") as file:
	lines = [int(x) for x in file.readlines()]

newArr = []
for i in range(len(lines)-2):
	newArr += [sum(lines[i:i+3])]

print("\n".join([str(x) for x in newArr]))
