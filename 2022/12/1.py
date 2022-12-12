from collections import *

with open("input", "r") as f:
	m = f.read().split("\n")[:-1]

DIRS = [
    (1, 0),
    (0, -1),
    (-1, 0),
    (0, 1),
]

def bfs(src, tgt, neighbours):
	q = deque([src])

	parent = {}

	while q:
		cur = q.popleft()
		if cur == tgt: break

		for n in neighbours[cur]:
			if n in parent: continue
			parent[n] = cur
			q.append(n)

	if tgt not in parent:
		return None

	pos = tgt
	path = []
	while pos != src:
		path.append(pos)
		pos = parent[pos]
	path.append(src)
	path.reverse()
	return path

board = {}
for y, l in enumerate(m):
	for x, c in enumerate(l):
		board[x,y] = c
		if c == "S":
			board[x,y] = "a"
			source = (x,y)
		elif c == "E":
			board[x,y] = "z"
			destination = (x,y)

print(board)

def get_neighbours(c):
    x, y = c
    adjacent = []
    for xm, ym in DIRS:
        adj = (x + xm, y + ym)
        if adj not in board:
            continue
        if ord(board[c]) + 1 >= ord(board[adj]):
            adjacent.append(adj)
    return adjacent

neighbours = {c: get_neighbours(c) for c in board}

print(len(bfs( source, destination, neighbours)) -1)

srcs = [k for k, v in board.items() if v == 'a' and ('b' in [board[n] for n in neighbours[k]])]
print(min([len(bfs(s, destination, neighbours)) - 1 for s in srcs]))
