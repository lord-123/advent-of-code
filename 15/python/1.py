import math
with open("input", "r") as file:
	nodes = [[int(x) for x in y[:-1]] for y in file.readlines()]

unvisited = { (i, j) for i in range(len(nodes)) for j in range(len(nodes[0])) }

distances = [[math.inf for i in range(len(nodes[0]))] for j in range(len(nodes))]
distances[0][0] = 0

current = (0, 0)
unvisited.remove((0,0))

while current != (len(nodes)-1, len(nodes[0])-1):
	for x in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
		i = current[0] + x[0]
		j = current[1] + x[1]

		if not (i < 0 or j < 0 or i >= len(nodes) or j >= len(nodes[0])):
			k = distances[current[0]][current[1]] + nodes[i][j] 
			if k < distances[i][j]:
				distances[i][j] = k
		
	unvisited.discard(current)
	current = min(unvisited, key=lambda x:distances[x[0]][x[1]])
	#for y in distances:
	#	print(y)

print(distances[-1][-1])
