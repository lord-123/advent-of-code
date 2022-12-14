with open("input", "r") as f:
	rock = []
	for l in f.read().split("\n")[:-1]:
		rock += [[list(map(int, x.split(","))) for x in l.split(" -> ")]]

print(rock)

solid = set()
for x in rock:
	prev = x[0]
	for r in x[1:]:
		if prev[0] == r[0]:
			shift = 1 if r[1] > prev[1] else -1
			solid |= set([(prev[0], i) for i in range(prev[1], r[1] + shift, shift)])
		else:
			shift = 1 if r[0] > prev[0] else -1
			solid |= set([(i, prev[1]) for i in range(prev[0], r[0] + shift, shift)])
		prev = r

floor = max(solid, key=lambda x: x[1])[1] + 2
print(solid)

count = 0

def sim_sand():
	global count
	grain = [500, 0]

	while grain[1] < max(solid, key=lambda x: x[1])[1]:
		if (grain[0], grain[1]+1) not in solid:
			grain[1]+=1
		elif (grain[0]-1, grain[1]+1) not in solid:
			grain[0]-=1
			grain[1]+=1
		elif (grain[0]+1, grain[1]+1) not in solid:
			grain[0]+=1
			grain[1]+=1
		else:
			solid.add(tuple(grain))
			count += 1
			return True
	return False

print(len(solid))

con = True
while con:
	con = sim_sand()

print(len(solid), count)
