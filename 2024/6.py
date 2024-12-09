from util import *

ll = readlines("6.in")
n = len(ll)
m = len(ll[0])

walls = set()

for i, l in enumerate(ll):
    for j, x in enumerate(l):
        if x == "#":
            walls.add((i, j))
        elif x == "^":
            guard = (i, j)

def traverse(guard):
    d = 3
    seen = set()
    while guard[0] >= 0 and guard[1] >= 0 \
        and guard[0] < n and guard[1] < m:
        seen.add(guard)
        f = (guard[0]+DIRS[d][0], guard[1]+DIRS[d][1])
        if f in walls:
            d = (d+1)%4
            continue
        guard = f
    return seen

# p1
s1 = traverse(guard)
print(len(s1))

def traverse2(guard):
    d = 3
    seen = set()
    while guard[0] >= 0 and guard[1] >= 0 \
        and guard[0] < n and guard[1] < m:
        if (guard, d) in seen:
            return True
        seen.add((guard, d))
        f = (guard[0]+DIRS[d][0], guard[1]+DIRS[d][1])
        if f in walls:
            d = (d+1)%4
            continue
        guard = f
    return False

# p2
s = 0
for x in s1:
    walls.add(x)
    if traverse2(guard):
        s += 1
    walls.remove(x)
print(s)