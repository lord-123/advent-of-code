from collections import defaultdict
with open("input", "r") as file:
	m = file.read()[:-1].split("\n")

elves = [[x, y]  for y,t in enumerate(m)for x,v in enumerate(t) if v == "#"]

print(elves)

ALL_DIRS = ((0, 1),
		(1, 1),
		(1, 0),
		(1, -1),
		(0, -1),
		(-1, -1),
		(-1, 0),
		(-1, 1))

DIRS = ((0, -1),
		(0, 1),
		(-1, 0),
		(1, 0))

moves =1

def round(state, startdir):
	global moves
	proposals = defaultdict(list)
	for elf in state:
		proposing = not all([[elf[0]+x, elf[1]+y] not in elves for x,y in ALL_DIRS])
		if not proposing:
			#print("not proposing", elf)
			continue

		for dx, dy in [DIRS[(i+startdir)%len(DIRS)] for i in range(len(DIRS))]:
			#print("cheking", elf, [dx, dy], [[elf[0]+(dx if dx!=0 else shift), elf[1]+(dy if dy!=0 else shift)] not in elves for shift in [-1, 0, 1]])
			if all([[elf[0]+(dx if dx!=0 else shift), elf[1]+(dy if dy!=0 else shift)] not in elves for shift in [-1, 0, 1]]):
				proposals[elf[0]+dx, elf[1]+dy] += [elf]
				break
	
	#print(proposals)
	moves = 0
	for p in proposals:
		if len(proposals[p]) == 1:
			#print("moving", proposals[p], p)
			state.remove(proposals[p][0])
			state += [list(p)]
			moves += 1
	return state

# p1
"""
state = elves
for i in range(10):
	state = round(state, i%len(DIRS))
print(state)

minx = min(x for x,y in elves)
maxx = max(x for x,y in elves)
miny = min(y for x,y in elves)
maxy = max(y for x,y in elves)

print([minx, maxx], [miny, maxy])
print("p1", (maxx-minx+1)*(maxy-miny+1)-len(elves))
"""
# p2
state = elves
i = 0
while moves > 0:
	state = round(state, i%len(DIRS))
	print(i)
	i+=1


print("p2", i)
