from util import *

h = readlines("12.in")

board = {}
for y, l in enumerate(h):
	for x, c in enumerate(l):
		board[x,y] = c
		if c == "S":
			board[x,y] = "a"
			source = (x,y)
		elif c == "E":
			board[x,y] = "z"
			target = (x,y)

def neighbours(p):
	n = []
	for x in adjacents(p):
		if x not in board: continue
		if ord(board[p]) + 1 >= ord(board[x]):
			n += [x]
	return n

n = {x: neighbours(x) for x in board}

print("p1", len(bfs(source, target, n))-1)

sources = [p for p in board if board[p] == "a" and "b" in [board[a] for a in neighbours(p)]]
print("p2", min(len(bfs(s, target, n)) for s in sources) - 1)
