with open("input", "r") as f:
	n = tuple((x*811589153, i) for i, x in enumerate(map(int, f.read()[:-1].split("\n"))))

movements = {i: x for (x, i) in n}
new = {i: x for (x, i) in n}

class doubledict(dict):
	def __setitem__(self, key, val):
		dict.__setitem__(self, key, val)
		dict.__setitem__(self, val, key)
	
	def __delitem__(self, key):
		dict.__delitem__(self, self[key])
		dict.__delitem__(self, key)

d = doubledict()

for x, i in n:
	d[i] = (x, i)

points = {(x, i): i for x,i in n}

def printd():
	print([d[j][0] for j in range(len(n))])
printd()
for _ in range(10):
	for x, i in n:
		idx = d[x, i]

		nidx = (idx+x)%(len(n)-1)

		if nidx > idx:
			move = 1
			for pos in range(idx, nidx):
				nxt = (pos+move)%len(n)
				d[pos] = d[nxt]
				pos += 1
				pos %= len(n)
			d[nidx] = (x, i)
		else:
			move = -1
			for pos in range(idx, nidx, -1):
				nxt = (pos+move)%len(n)
				d[pos] = d[nxt]
				pos -= 1
				pos %= len(n)
			d[nidx] = (x,i)
		print(i)


printd()

for e in range(len(n)):
	if d[e][0] == 0:
		base = e

print(base)

print(d[1000%len(n)])

print(d[(base+1000)%len(n)][0]+d[(base+2000)%len(n)][0]+d[(base+3000)%len(n)][0])
