import re
from collections import *
from z3 import *

# constants
INF = float("inf")

DIRS = (( 0,  1),
		( 1,  0),
		( 0, -1),
		(-1,  0))

# parsing
def read(fname):
	with open(fname, "r") as f:
		s = f.read()[:-1]
	return s

def readlines(fname):
	return read(fname).split("\n")

def readstanzas(fname):
	return [s.split("\n") for s in read(fname).split("\n\n")]

def ints(s):
	return tmap(int, re.findall(r"-?\d+", s))

def readlinesints(fname):
	return tmap(ints, readlines(fname))

def lmap(f, it):
	return list(map(f, it))

def tmap(f, it):
	return tuple(map(f, it))

def flat(it):
	return [x for sub in it for x in sub]

# vectors
def manhattan(a, b):
	return sum(abs(a[i]-b[i]) for i in range(len(a)))

def manhattanz3(a, b):
	return Sum(*[Abs(a[i]-b[i]) for i in range(len(a))])

def adjacents(v):
	c = list(v[::])
	for i, x in enumerate(c):
		c[i] += 1
		yield tuple(c)
		c[i] -= 2
		yield tuple(c)
		c[i] += 1

# graph
def floodfill(blocked, start, bound=(-INF, INF)):
	filled = set()
	queue = [tuple(start)]
	lowb, highb = bound
	while len(queue) > 0:
		n = queue.pop(0)
		if any(x < lowb or x > highb for x in n): continue
		if n in blocked or n in filled: continue
		filled.add(n)
		queue += adjacents(n)
	return filled

def bfs(source, target, neighbours):
	q = deque([source])
	parent = {}

	while q:
		current = q.popleft()
		if current == target: break

		for n in neighbours[current]:
			if n in parent: continue
			parent[n] = current
			q.append(n)

	if target not in parent:
		return None

	pos = target
	path = []
	while pos != source:
		path += [pos]
		pos = parent[pos]
	path += [source]
	path.reverse()
	return path

# range
def merge(ranges):
	out = []
	for low, high in sorted(ranges):
		if out and out[-1][1] >= low-1:
			out[-1][1] = max(out[-1][1], high)
		else:
			out += [[low, high]]
	return out

# z3
def all_solutions(solver):
	s = solver.translate(main_ctx())
	while s.check() == sat:
		m = s.model()
		s.add(Or([ f() != m[f] for f in m.decls() if f.arity() == 0]))
		yield m
