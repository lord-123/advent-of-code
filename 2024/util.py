import re
import operator
import numpy
from collections import *
from z3 import *

# constants
INF = float("inf")

DIRS = (( 0,  1),
		( 1,  0),
		( 0, -1),
		(-1,  0))

OPS = {
	"+": operator.add,
	"-": operator.sub,
	"/": operator.truediv,
	"*": operator.mul,

	"==": operator.eq
}

# parsing
def read(fname):
	with open(fname, "r") as f:
		s = f.read()[:-1]
	return s

def readlines(fname):
	return read(fname).split("\n")

def readstanzas(fname):
	return [s.split("\n") for s in read(fname).split("\n\n")]

def words(s):
	return tmap(str, s.split(" "))

def readlineswords(fname):
	return tmap(words, readlines(fname))

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

def flatmap(f, it):
	return flat(lmap(f, it))

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

# array
def groups(l, f):
	g = defaultdict(list)
	for y in range(len(l)):
		for x in range(len(l[y])):
			g[f(x,y)] += [l[y][x]]
	return lmap(g.get, sorted(g))

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

def graphdist(adj, weights = defaultdict(lambda: 1)):
	dist = defaultdict(lambda: INF)
	for v in adj:
		for u in adj[v]:
			dist[v,u] = weights[v,u]
		dist[v,v] = 0
	for u in adj:
		for v in adj:
			for w in adj:
				dist[v,w] = min(dist[v,w], dist[v,u] + dist[u,w])
	return dist

def graphcull(adj, f): # culls if true
	new = {x: tuple(y for y in adj[x] if not f(y)) for x in adj if not f(x)}
	return new

# range
def merge(ranges):
	out = []
	for low, high in sorted(ranges):
		if out and out[-1][1] >= low-1:
			out[-1][1] = max(out[-1][1], high)
		else:
			out += [[low, high]]
	return out

# instruction evaluation
def eval_tree(tree):
	if "literal" in tree: return tree["literal"]

	return tree["operator"](*tuple(eval_tree(x) for x in tree["args"]))

"""
	return tree["operator"](eval_bintree(tree["left"]), eval_bintree(tree["right"]))
"""
# z3
def all_solutions(solver):
	s = solver.translate(main_ctx())
	while s.check() == sat:
		m = s.model()
		s.add(Or([ f() != m[f] for f in m.decls() if f.arity() == 0]))
		yield m
