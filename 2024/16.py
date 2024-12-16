from util import *
from collections import deque

ma= readlines("16.in")

spaces = set()

for i, l in enumerate(ma):
    for j, c in enumerate(l):
        if c == "#": continue

        spaces.add((i,j))

        if c == "E": end = (i,j)
        if c == "S": start = (i,j)
print(end)
unvisited = {(start, 0)}
#dist = {s: INF for s in unvisited}
dist = defaultdict(lambda: INF)
dist[start, 0] = 0
#print(unvisited)
#print(((11,1),3) in unvisited)
prev = defaultdict(list)
while unvisited:
    #print(len(unvisited))
    node, d = min(unvisited, key=lambda s: dist[s])
    unvisited.remove((node, d))
    curr_dist = dist[node, d]
    if curr_dist == INF: break

    # update neighbours
    for x in (-1,0,1):
        f = (d+x)%4
        n = tuple(add(node, DIRS[f]))
        if n in spaces:
            a = curr_dist+(abs(x)*1000)+1
            if a == dist[n, f]:
                prev[n, f] += [(node, d)]
            if a < dist[n, f]:
                dist[n, f] = a
                prev[n, f] = [(node, d)]
                unvisited.add((n, f))
            
    # n = tuple(add(node, DIRS[d]))
    # if (n, d) in unvisited:
    #     if dist[n,d] > curr_dist+1:
    #         dist[n,d] = curr_dist+1
    #         prev[n,d] = (node,d)
    #     #dist[n, d] = min(dist[n, d], curr_dist+1)

    # l = (d-1)%4
    # n = tuple(add(node, DIRS[l]))
    # if (n, l) in unvisited:
    #     dist[n, l] = min(dist[n, l], curr_dist+1001)

    # r = (d+1)%4
    # n = tuple(add(node, DIRS[r]))
    # if (n, r) in unvisited:
    #     dist[n, r] = min(dist[n, r], curr_dist+1001)

    
    #input()

# p1
path = min([dist[end, x] for x in [0,1,2,3]])
print(path)

dirs = [i for i in [0,1,2,3] if dist[end, i] == path]
#print(dirs)
#print(prev)
q = deque([(end, d) for d in dirs])
visited = set()
while len(q) > 0:
    c = q.popleft()
    if c in visited: continue
    visited.add(c)
    x = prev[c]
    for x in prev[c]:
        print("x", x)
        if x not in visited:
            q.append(x)

visited = set([x[0] for x in visited])

def draw():
    s = ""
    for i in range(len(ma)):
        for j in range(len(ma[0])):
            c = "."
            if (i,j) in visited: c = "O"
            s += c
        s += "\n"
    print(s)

draw()
print(visited)
print(len(visited))