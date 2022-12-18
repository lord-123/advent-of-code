import re
from z3 import *

# constants
INF = float("inf")

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
	return map(int, re.findall(r"-?\d+", s))

def lmap(f, it):
	return list(map(f, it))

# vectors
def manhattan(a, b):
	return sum(abs(a[i]-b[i]) for i in range(len(a)))

def manhattanz3(a, b):
	return Sum(*[Abs(a[i]-b[i]) for i in range(len(a))])

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
