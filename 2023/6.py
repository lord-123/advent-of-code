from util import *
from z3 import *

fname = "input6"
#fname = "example6"

ll = readlines(fname)

times = tmap(int, ll[0].split()[1:])
distances = tmap(int, ll[1].split()[1:])

def f(t, d):
    for i in range(t//2):
        if (t-i)*i > d:
            return t-2*i+1

# p1
p1 = 1

for t,d in zip(times, distances):
    p1 *= f(t,d)

print(f"p1: {p1}")

# p2
t = int("".join(ll[0].split()[1:]))
d = int("".join(ll[1].split()[1:]))

o = Optimize()
i = Int("i")
o.add(i > 0)
o.add((t-i)*i > d)
o.minimize(i)
o.check()
p2 = o.model().evaluate(t-2*i+1)

print(f"p2: {p2}")
