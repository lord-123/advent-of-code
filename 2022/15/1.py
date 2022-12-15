with open("input", "r") as f:
	sensors = [x.split(": closest beacon is at ") for x in f.read()[:-1].split("\n")]

sensors = [[x[0][10:], x[1]] for x in sensors]
sensors = [list(map(lambda x: list(map(lambda z: int(z[2:]), x.split(", "))), y)) for y in sensors]

def manhattan(a, b):
	return abs(a[0]-b[0])+abs(a[1]-b[1])

covered = set()
beacons = set([tuple(x[1]) for x in sensors])

#sensors = [[[8,7], [2, 10]]]

for i,s in enumerate(sensors):
	print(i)
	sensor = s[0]
	beacon = s[1]
	m = manhattan(sensor, beacon)
	#print(m)
	for i in range(0, m+1):
		for j in range(i*2+1):
			#print((sensor[0]-i+j, sensor[1]-(m-i)))
			covered.add((sensor[0]-i+j, sensor[1]-(m-i)))
			covered.add((sensor[0]-i+j, sensor[1]+(m-i)))
covered -= beacons
print(len([x for x in covered if x[1] == 20000]))
