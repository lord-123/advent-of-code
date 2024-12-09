from util import *
from itertools import combinations

ll = readlines("8.in")
n = len(ll)
m = len(ll[0])
print(n,m)

antennas = defaultdict(list)

for i, l in enumerate(ll):
    for j, x in enumerate(l):
        if x != ".":
            antennas[x] += [(i, j)]

#print(antennas)

def inmap(p):
    x,y =p
    if x < 0 or y < 0:
        return False
    if x >=n or y >= m:
        return False
    return True

an = set()
for k in antennas:
    c = combinations(antennas[k], 2)
    for a, b in c:
        a1,a2 = a
        b1,b2=b

        diff = (a1-b1, a2-b2)
        d1,d2 = diff
        #print(a,b, diff)

        x = (a1+d1, a2+d2)
        y = (b1-d1, b2-d2)

        for p in (x,y):
            if inmap(p):
                an.add(p)

# p1
print(sorted(list(an)), len(an))

def gen_nodes(p, v):
    if v[0] == 0:
        v[1] = 1 if v[1] >= 1 else -1
    if v[1] == 0:
        v[0] = 1 if v[0] >= 1 else -1
    c = (p[0]+v[0], p[1]+v[1])
    while inmap(c):
        yield c
        c = (c[0]+v[0], c[1]+v[1])
    c = (p[0]-v[0], p[1]-v[1])
    while inmap(c):
        yield c
        c = (c[0]-v[0], c[1]-v[1])

an = set()
for k in antennas:
    if len(antennas[k]) > 1:
        an.update(antennas[k])
    c = combinations(antennas[k], 2)
    for a, b in c:
        a1,a2 = a
        b1,b2=b

        diff = (a1-b1, a2-b2)
        d1,d2 = diff

        x = (a1+d1, a2+d2)
        y = (b1-d1, b2-d2)

        for p in gen_nodes(a, diff):
            an.add(p)

# p1
print(sorted(list(an)), len(an))