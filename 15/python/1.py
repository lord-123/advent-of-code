import math
with open("input", "r") as file:
	nodes = [[int(x) for x in y[:-1]] for y in file.readlines()]

print(len(nodes), len(nodes[0]))

for j,x in enumerate(nodes):
	k = [[y+i-9 if y+i > 9 else y+i for y in x] for i in range(5)]
	k = [x for l in k for x in l]
	nodes[j] = k

l = len(nodes)
for i in range(1,5):
	for x in nodes[:l]:
		nodes += [[y+i-9 if y+i > 9 else y+i for y in x]]

print(len(nodes), len(nodes[1]))

with open("test_full", "r") as file:
	test = [[int(x) for x in y[:-1]] for y in file.readlines()]

print(test == nodes)
print(len(nodes))
print(len(nodes[0]))

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
		
	print(current)
	unvisited.discard(current)
	current = min(unvisited, key=lambda x:distances[x[0]][x[1]])

print(distances)
print(distances[-1][-1])
