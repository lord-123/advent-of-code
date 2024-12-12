from util import *
from itertools import groupby

ll = readlines("12.in")

regions = defaultdict(set)
plots = dict()

rc = 0

for i, l in enumerate(ll):
    for j, x in enumerate(l):
        plots[i, j] = x

seen = set()
#print(plots)

for p in plots:
    if p in seen:
        continue

    t = plots[p]

    q = deque([p])
    while q:
        curr = q.pop()
        if curr in seen:
            continue
        seen.add(curr)
        regions[rc].add(curr)

        for x in adjacents(curr):
            if x in seen or x not in plots: continue
            if plots[x] == t:
                q.append(x)
    rc += 1

def perimeter(region):
    s = 0
    for x in region:
        for y in adjacents(x):
            if y not in region:
                s += 1

    return s

def price(region):
    return len(region) * perimeter(region)

# p1
print(sum(price(regions[x]) for x in regions))

def sides(region):
    edges = defaultdict(set)
    for p in region:
        for a in DIRS:
            x = (a[0]+p[0], a[1]+p[1])
            if x not in region:
                edges[a].add(p)
    #print(edges)
    c = 0
    for d in edges:
        horizontal = d[0] == 0
        l = sorted([(b,a) if horizontal else (a,b) for a,b in edges[d]], key=lambda x: (x[0], x[1]))
        prev = (-1,-1)
        for x in l:
            if x[0] != prev[0] or x[1] != prev[1] + 1:
                c += 1
            prev = x
    return c

def price(region):
    return len(region) * sides(region)

print(sum(price(regions[x]) for x in regions))