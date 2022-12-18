from util import *

cubes = readlinesints("18.in")

adj = flat(map(adjacents, cubes))

covered = 0
for a in adj:
	if a in cubes:
		covered += 1

print("p1", 6*len(cubes)-covered)

air = floodfill(cubes, (0, 0, 0), (-2, 22))

s = [x for x in adj if x not in cubes and x in air]

print("p2", len(s))
