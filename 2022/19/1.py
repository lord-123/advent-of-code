from functools import cache
bp = []
b = {}
with open("input", "r") as file:
	ll = [x.split(" ") for x in file.read()[:-1].split("\n")]
	for l in ll:
		k = tuple([int(l[1][:-1]), int(l[6]), int(l[12]), int(l[18]), int(l[21]), int(l[27]), int(l[30])])
		bp += [((k[1]), (k[2]), (k[3], k[4]), (k[5], k[6]))]
		b[k[0]] = {"ore": {"ore": k[1]}, "clay": {"ore": k[2]}, "obsidian": {"ore": k[3], "clay": k[4]}, "geode": {"ore": k[5], "obsidian": k[6]}}

# state = (ore, clay, obsidian, geodes, orec, clayc, obc, geoc, time)
# rule = (ore, ore, (ore, clay), (ore, obsidian))
seen_n = set()
def get_neighbours(x, rule):
	if x in seen_n: return []
	seen_n.add(x)
	ore, clay, obsidian, geodes, orec, clayc, obc, geoc= x
	#if time <= 0: return
	#time -= 1

	max_ore = max(rule[0], rule[1], rule[2][0], rule[3][0])
	max_clay = rule[2][1]
	max_obs = rule[3][1]

	n = []

	if ore >= rule[3][0] and obsidian >= rule[3][1]: #make geode robot
		n += [(ore-rule[3][0]+orec, clay+clayc, obsidian-rule[3][1]+obc, geodes+geoc, orec, clayc, obc, geoc+1)]
	else:
		n += [(ore+orec, clay+clayc, obsidian+obc, geodes+geoc, orec, clayc, obc, geoc)]

		if ore >= rule[2][0] and clay >= rule[2][1] and not (obc >= max_obs): # make obsidian bot
		  n += [(ore-rule[2][0]+orec, clay-rule[2][1]+clayc, obsidian+obc, geodes+geoc, orec, clayc, obc+1, geoc)]
		if ore >= rule[1] and not (clayc >= max_clay):
		  n += [(ore-rule[1]+orec, clay+clayc, obsidian+obc, geodes+geoc, orec, clayc+1, obc, geoc)]
		if ore >= rule[0] and not (orec >= max_ore): # make ore bot
			n += [(ore-rule[0]+orec, clay+clayc, obsidian+obc, geodes+geoc, orec+1, clayc, obc, geoc)]
	
	return n

start_state = (0, 0, 0, 0, 1, 0, 0, 0)

@cache
def find(current, time, b):
	ore, clay, obsidian, geodes, orec, clayc, obc, geoc= current
	
	q = [current]
	seen = set()


	for i in range(time):
		new_q = []
		while q:
			current = q.pop()

			for n in get_neighbours(current, b):
				if n in seen: continue
				new_q += [n]
				seen.add(n)
		q = new_q
		print(i)

	return (max(x[3] for x in q))

# p1
"""
s = 0
for i,x in enumerate(bp, 1):
	seen_n = set()
	s += find(start_state, 24, x)*i
	print(s)
"""
# p2
m = 1
for i,x in enumerate(bp[:3], 1):
	lowest = 32
	seen_n = set()
	m *= find(start_state, 32, x,)
	print(m)
print("finished p2")
"""
print(get_neighbours(start_state, bp[0]))
print(find(start_state, 24, bp[0]))
print(list(get_neighbours((4,25,7,2,1,4,2,1), bp[0])))
print(list(get_neighbours((3,29,2,3,1,4,2,2), bp[0])))

print(list(get_neighbours(start_state, bp[1])))
"""
