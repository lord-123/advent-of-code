from util import *

i = tmap(ints, readlines("1.in"))

#p1
l = sorted([x[0] for x in i])
r = sorted([x[1] for x in i])

out = sum([abs(a-b) for a,b in zip(l,r)])
print(out)

#p2
cl = Counter(l)
cr = Counter(r)

s = 0
for x in cl:
    if cr[x] == 0: continue

    s += x*cr[x]*cl[x]
print(s)