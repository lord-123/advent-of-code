with open("input", "r") as f:
	sensors = [x.split(": closest beacon is at ") for x in f.read()[:-1].split("\n")]

sensors = [[x[0][10:], x[1]] for x in sensors]
sensors = [list(map(lambda x: list(map(lambda z: int(z[2:]), x.split(", "))), y)) for y in sensors]

def manhattan(a, b):
	return abs(a[0]-b[0])+abs(a[1]-b[1])

def merge(l):
	l = sorted(l)
	nl = [l[0]]
	for x in l[1:]:
		if nl[-1][1] + 1 >= x[0]:
			if nl[-1][1] < x[1]:
				nl[-1][1] = x[1]
		else:
			nl += [x]
	return nl

beacons = set([tuple(x[1]) for x in sensors])

checking = 2000000
maxpos = 4000000

ranges = [[] for x in range(maxpos)]

for i,s in enumerate(sensors):
	sensor = s[0]
	beacon = s[1]
	m = manhattan(sensor, beacon)

	for j in range(sensor[1]-m, sensor[1]+m+1):
		if j < 0: continue
		if j >= maxpos: break
		size = m-abs(j-sensor[1])
		r = sorted([sensor[0]-size, sensor[0]+size])
		ranges[j] += [r]
		ranges[j] = merge(ranges[j])
		#if j == 11: print(sensor, ranges[j])

#p1
"""
for b in beacons:
	if b[1] != checking: continue
	for i, r in enumerate(ranges[checking]):
		if r[0] <= b[0] and b[0] <= r[1]:
			temp = r[1]
			r[1] = b[0]-1
			ranges[checking] += [[b[0]+1, temp]]
ranges[checking] = merge(ranges[checking])

print(sum([x[1]-x[0]+1 for x in ranges[checking]]))
"""
# p2
for i, r in enumerate(ranges):
	if r[0][0] < 0:
		r[0][0] = 0
	if r[-1][1] > maxpos:
		r[-1][1] = maxpos

for i, r in enumerate(ranges):
	if len(r) > 1:
		print(i+(r[0][1]+1)*4000000)
		break
