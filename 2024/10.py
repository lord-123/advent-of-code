from util import *

ma = lmap(lambda x: lmap(int, x), readlines("10.in"))
n = len(ma)
m = len(ma[0])
print(ma)

g = defaultdict(list)
h = []

for i, ll in enumerate(ma):
    for j, v in enumerate(ll):
        if v == 0:
            h += [(i, j)]
        for x, y in adjacents((i, j)):
            if x < 0 or y < 0 or x > n - 1 or y > m - 1:
                continue
            if ma[x][y] == v+1:
                g[(i,j)] += [(x,y)]

def score(p, depth = 0):
    seen = set()
    q = deque([(p, 0)])
    s = 0

    while q:
        l, depth = q.pop()
        if l in seen:
            continue
        seen.add(l)
        if depth == 9:
            s += 1
            continue

        for x in g[l]:
            if x not in seen:
                q.append((x, depth+1))

    return s

print(h)
print(g)

s = lmap(score, h)
print(sum(s))

def score(p, depth = 0):
    if depth == 9:
        return 1
    return sum([score(x, depth+1) for x in g[p]])

s = lmap(score, h)
print(sum(s))