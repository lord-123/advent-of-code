with open("input", "r") as f:
	n = tuple((x, i) for i, x in enumerate(map(int, f.read()[:-1].split("\n"))))

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
for x, i in n:
	p = d[x, i]

	j = 0
	count = 0
	for j in range(abs(x)):
		idx = d[x, i]
		if x > 0:
			nidx = (idx+1)%len(n)
			if idx == len(n)-2:
				for k in range(len(n)-2, 0, -1):
					d[k] = d[k-1]

				d[0] = (x,i)
				continue
		else:
			nidx = (idx-1)%len(n)
			if idx == 1:
				for k in range(2, len(n)):
					d[k-1] = d[k]

				d[len(n)-1] = (x,i)
				continue
		d[idx] = d[nidx]
		d[nidx] = (x, i)


for e in range(len(n)):
	if d[e][0] == 0:
		base = e

print(base)

print(d[1000%len(n)])

print(d[(base+1000)%len(n)][0]+d[(base+2000)%len(n)][0]+d[(base+3000)%len(n)][0])
