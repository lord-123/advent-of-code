with open("input", "r") as file:
	paths = [set(y.strip("\n").split("-")) for y in file.readlines()]

print(paths)

def f(p, cave="end", visited=["end"], paths=[]):
	count = 0
	new_visited = visited + [cave]
	print(f"visited: {new_visited}")
	next_caves = [[x for x in y if x != cave][0] for y in p if cave in y]
	#print(f"{cave}: {next_caves}")
	next_caves = [x for x in next_caves if x not in visited or x.isupper()]
	print(f"{cave}: {next_caves}")
	for x in next_caves:
		if x == "start":

			count += 1
		if x != "start":
			count += f(p, x, new_visited)
	
	return count

print(f(paths))
