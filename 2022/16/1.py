from parse import parse
from collections import defaultdict
from functools import cache
with open("input", "r") as f:
	i = [parse("Valve {valve} has flow rate={flow:d}; tunnel{}lead{}to valve{}{leads}", x) for x in f.read().split("\n")[:-1]]
	adj = {x["valve"]: {a: 1 for a in list(map(str.strip, x["leads"].split(", ")))} for x in i}
	flow = {x["valve"]: x["flow"] for x in i}
marked = []
for x in adj:
	if flow[x] == 0 and x != "AA":
		for a in adj[x]:
			for b in adj[x]:
				if b==a:continue
				adj[a][b]=adj[x][a]+adj[x][b]
		marked+=[ x]
for x in marked:
	del adj[x]

newadj = {}
for x in adj:
	newadj[x] = {}
	newadj[x] = {k: adj[x][k] for k in adj[x] if k not in marked}
adj = newadj
print(adj)

dist = defaultdict(lambda: float("inf"))
for v in adj:
	for u in adj[v]:
		dist[(v,u)]=adj[v][u]
for v in adj:
	dist[(v,v)] = 0
for k in adj:
	for i in adj:
		for j in adj:
			if dist[(i, j)] > dist[(i,k)] + dist[(k,j)]:
				dist[(i,j)] = dist[(i,k)] + dist[(k,j)]

print(dist)

all_keys = tuple([x for x in adj])
print(all_keys)
@cache
def find(current, time, mask):
	if time <= 0: return 0

	best = 0
	bit = 1
	i = 0
	while bit <= mask:
		if bit & mask:
			x = all_keys[i]
			if time + 1 >= dist[(current, x)]:
				newtime = time-dist[(current, x)]-1
				best = max(best, find(x, newtime, mask-bit) + newtime*flow[x])
		bit *= 2
		i+=1
	
	return best

#p1
print(find("AA", 30, (1 << len(all_keys))-1))

#p2
m = 0
prev = 0
all_mask = (1<<len(all_keys))-1
for mask in range(all_mask+1):
	m = max(m, find("AA", 26, mask) + find("AA", 26, all_mask-mask))
	if m > prev: print(f"current max: {m} percent searched: {100*mask/all_mask}")
	prev = m
print("finally:", m)
