from util import *
from collections import defaultdict

nums = tmap(int, readlines("22.in"))

def f(x, n=1):
	for i in range(n):
		x = (x ^ (x * 64)) % 16777216
		x = (x ^ (x // 32)) % 16777216
		x = (x ^(x*2048)) % 16777216
	return x

# p1
print(sum([f(x, 2000) for x in nums]))

def f(x, c=2000):
	v = defaultdict(set)
	changes = []
	prev = x % 10
	seen = set()

	for _ in range(c):
		x = (x ^ (x * 64)) % 16777216
		x = (x ^ (x // 32)) % 16777216
		x = (x ^(x*2048)) % 16777216
		
		unit = x % 10
		changes = changes[-3:] + [unit - prev]
		prev = unit
		if (k:=tuple(changes)) in seen or len(changes) < 4: continue
		v[k] = unit
		seen.add(k)

	return v

m = defaultdict(int)
for n in nums:
	v = f(n)
	for x in v:
		m[x] += v[x]

k=(max(m, key=lambda x: m[x]))
# p2
print(m[k])
