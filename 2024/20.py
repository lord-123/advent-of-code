from util import *
from collections import defaultdict
import heapq

ll = readlines("20.in")

walls = set()

for i, l, in enumerate(ll):
	for j, c in enumerate(l):
		if c == "#": walls.add((i,j))

		if c == "S": start = (i, j)
		if c == "E": end = (i, j)

# get path
dist = defaultdict(lambda: INF)
prev = dict()
seen = set()
q = [(0, start)]
heapq.heapify(q)

while len(q) > 0:
	#print(q)
	d, cur = heapq.heappop(q)
	if cur == end: break
	if d == INF: break
	if cur in seen: continue
	seen.add(cur)

	nodes = [x for x in adjacents(cur) if x not in walls]

	for n in nodes:
		a = d + 1
		if a < dist[n]:
			heapq.heappush(q, (a, n))
			dist[n] = a
			prev[n] = cur

path = []
c = end
while c != start:
	path = [c] + path
	c = prev[c]
path = [start] + path

# could probably be done faster
c = 0
for i, x in enumerate(path[:-2]):
	d = [j+1 for j, y in enumerate(path[i+3:]) if manhattan(x,y) == 2 and j+1 >= 100]
	c += len(d)

print(c)

c = 0
times = defaultdict(int)
for i, x in enumerate(path[:-2]):
	for j, y in enumerate(path[i+3:]):
		d = manhattan(x,y)
		if d > 20: continue
		time = j+3 - d
		if time < 100: continue
		times[time] += 1
		c += 1

#print(times)
print(c)
