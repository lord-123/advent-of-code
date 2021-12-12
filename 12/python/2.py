with open("input", "r") as file:
	paths = [set(y.strip("\n").split("-")) for y in file.readlines()]

print(paths)

def f(one_off, cave="start", visited=set()):
	if cave == "end": return 1
	if cave.islower(): visited.add(cave)
	next_caves = [[x for x in y if x != cave][0] for y in paths if cave in y]
	total = sum(f(one_off, i, visited) for i in next_caves if i not in visited)
	total += sum(f(i, i, visited) for i in next_caves if i in visited and i != "start") if one_off == " " else 0
	if cave != one_off: visited.discard(cave)
	return total

print(f(" "))
