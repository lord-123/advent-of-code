from util import *
from functools import cache

lines = readlines("16.in")

adj = {}
flow = {}
for l in lines:
	w = words(l)
	v = w[1]
	adj[v] = tuple(x[:2] for x in w[9:])
	flow[v] = ints(l)[0]

dist = graphdist(adj)

adj = graphcull(adj, lambda x: flow[x] == 0)

all_keys = tuple(x for x in adj)

@cache
def find(current, time, mask):
	best = 0
	bit = 1
	i = 0
	while bit <= mask:
		if bit & mask:
			x = all_keys[i]
			if time + 1 >= dist[current, x]:
				newtime = time - dist[current, x] - 1
				best = max(best, find(x, newtime, mask-bit) + newtime*flow[x])
		bit *= 2
		i += 1
	
	return best

all_mask = (1<<len(all_keys))-1

print("p1", find("AA", 30, all_mask))

m = 0
for mask in range(all_mask+1):
	m = max(m, 26, find("AA", 26, mask) + find("AA", 26, all_mask-mask))
print("p2", m)
