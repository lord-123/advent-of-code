with open("input","r") as f:
	cubes = [list(map(int, x.split(","))) for x in f.read()[:-1].split("\n")]

sides = 6*len(cubes)

covered = 0
for cube in cubes:
	for x in [-1,1]:
		if [cube[0] + x, cube[1], cube[2]] in cubes:
			covered += 1
	for y in [-1,1]:
		if [cube[0], cube[1] + y, cube[2]] in cubes:
			covered += 1
	for z in [-1,1]:
		if [cube[0], cube[1], cube[2] + z] in cubes:
			covered += 1

print(f"p1: {sides-covered}")

def adjacent(a):
	x,y,z = a
	return [[x + 1, y, z],
	        [x - 1, y, z],
            [x, y + 1, z],
            [x, y - 1, z],
            [x, y, z + 1],
            [x, y, z - 1]]


outer = set()
cubeset = set(tuple(x) for x in cubes)
q = [[0,0,0], [20, 20, 20], [20, 0, 20], [20, 0, 0], [20, 20, 0], [0, 0, 20], [0, 20, 20]]
while len(q) > 0:
	x,y,z = q.pop(0)
	if x < -5 or x > 50 or y < -5 or y > 50 or z < -5 or z > 50: continue
	if (x, y, z) in outer or (x, y, z) in cubeset: continue
	outer.add((x, y, z))
	q += [[x + 1, y, z]]
	q += [[x - 1, y, z]]
	q += [[x, y + 1, z]]
	q += [[x, y - 1, z]]
	q += [[x, y, z + 1]]
	q += [[x, y, z - 1]]

check = [i for sub in [adjacent(c) for c in cubeset] for i in sub]
s = [x for x in check if tuple(x) not in cubeset and tuple(x) in outer]

print(len(s))
