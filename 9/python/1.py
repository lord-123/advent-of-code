filename = input()
with open(filename, "r") as file:
	levels = [[int(x) for x in y if x != "\n"] for y in file.readlines()]

levels = [[10 for i in range(len(levels[0]))]] + levels
levels += [[10 for i in range(len(levels[0]))]]

for i in range(len(levels)):
	levels[i] = [10] + levels[i] + [10]

print("\n".join(str(x) for x in levels))

lowpoints = []
for i in range(len(levels)):
	for j in range(len(levels[i])):
		cur = levels[i][j]
		if cur < levels[i-1][j] and cur < levels[i+1][j] and cur < levels[i][j-1] and cur < levels[i][j+1]:
			lowpoints += [(i, j)]

#print(lowpoints)

print(sum(levels[i][j] + 1 for i,j in lowpoints))

basins = [[x < 9 for x in y] for y in levels]

n = len(basins)
m = len(basins[0])
total = 0

def flood(i, j):
	if i < 0 or j < 0 or i >=n or j>= m:
		return 0
	elif basins[i][j] == False:
		return 0

	basins[i][j] = False
	c = 1
	c+=flood(i+1,j)
	c+=flood(i,j+1)
	c+=flood(i-1,j)
	c+=flood(i,j-1)
	return c

sizes = []
for i in range(n):
	for j in range(m):
		if basins[i][j]:
			sizes+=[flood(i, j)]
			total += 1

#for i in basins:
#	print(" ".join("1" if x else "0" for x in i))

print(total)
print(sizes)
t = 1
for i in sorted(sizes)[-3:]:
	t *= i
print(t)
