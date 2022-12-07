with open("input", "r") as f:
	c = [x.strip("\n").split("\n") for x in f.read().split("$ ")][1:]

print(c)

files = { "/" : {} }

wd = ["/"]
for x in c:
	command = x[0].split(" ")
	if len(command) > 1:
		arg = command[1]
	command = command[0]

	print(command, arg)
	if command == "cd":
		if arg == "..":
			wd.pop(-1)
		elif arg == "/":
			wd = [arg]
		else:
			wd += [arg]
		print(wd)
	elif command == "ls":
		results = x[1:]
		print("results: ", results)

		f = files
		for key in wd:
			f = f[key]

		for r in [k.split(" ") for k in results]:
			if r[0] == "dir":
				f[r[1]] = {}
			else:
				f[r[1]] = int(r[0])

sizes = []
def size(d):
	global sizes
	s = 0
	for x in d:
		if type(d[x]) is int:
			s += d[x]
		else:
			s += size(d[x])

	sizes += [s]
	return s

s = size(files)
print("p1:", sum([x for x in sizes if x <= 100000]))

#p2
needed = 30000000 - (70000000 - s)
print("p2:", sorted([x for x in sizes if x>=needed])[0])
