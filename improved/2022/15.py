from util import *
from z3 import *

sensors = map(ints, readlines("15.in"))

#p1
ranges = []
#p2
x, y = Ints("x y")
s = Solver()
s.add(x>=0, y>=0, x<=4000000, y<=4000000)
for sx, sy, bx, by in sensors:
	bombd = manhattan((sx, sy), (bx, by))
	
	#p1
	d = bombd - abs(sy - 2000000)
	if d >= 0:
		ranges += [[sx-d, sx+d]]
	
	#p2
	s.add(bombd < manhattanz3((sx, sy), (x, y)))

ranges = merge(ranges)
s.check()

print("p1:", sum(hi-lo for lo, hi in ranges))
print("p2:", s.model().evaluate(x*4000000-y))
