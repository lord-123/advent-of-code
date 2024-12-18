from util import *
from collections import defaultdict
import heapq
from bisect import bisect_left

b = readlinesints("18.in")

size = 70

# walls = set(b[:12])
# walls.update([(-1, i) for i in range(size+1)])
# walls.update([(size+1, i) for i in range(size+1)])
# walls.update([(i, -1) for i in range(size+1)])
# walls.update([(i, size+1) for i in range(size+1)])

def dk(count):
    walls = set(b[:1024 + count])
    walls.update([(-1, i) for i in range(size+1)])
    walls.update([(size+1, i) for i in range(size+1)])
    walls.update([(i, -1) for i in range(size+1)])
    walls.update([(i, size+1) for i in range(size+1)])
    q = [(0, (0,0))]
    heapq.heapify(q)
    dist = defaultdict(lambda: INF)
    dist[0,0] = 0

    seen = set()

    while len(q) > 0:
        d, curr = heapq.heappop(q)
        #print(d,q)
        if curr == (size, size): break
        if curr in seen: continue
        seen.add(curr)
        if d == INF: break

        for x in adjacents(curr):
            if x in walls:
                continue

            a = d + 1
            if a < dist[x]:
                dist[x] = a
                heapq.heappush(q, (a, x))
    return dist[size,size]



# p1
print(dk(0))

# p2
print(",".join(map(str,b[1023+bisect_left(list(range(len(b)-1024)), INF, key=dk)])))