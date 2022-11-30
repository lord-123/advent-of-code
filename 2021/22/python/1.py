with open("input", "r") as file:
	lines = file.readlines()
	lines = [x.strip("\n") for x in lines]
	c = [x.split(" ")[0] for x in lines]
	a = [[tuple([int(z) for z in y[2:].split("..")]) for y in x.split(" ")[1].split(",")] for x in lines]

	steps = zip(c, a)

def crange(a, b):
	return range(a, b + 1 if a < b else b - 1, -1 if a > b else 1)

min_c = -50
max_c =  50

cubes = [[[0 for i in range(max_c-min_c+1)] for j in range(max_c-min_c+1)] for k in range(max_c-min_c+1)]

for c, a in steps:
	if a[0][0] < min_c or a[0][0] > max_c: break

	val = 1 if c=="on" else 0
	print(val)
	print(a)

	for i in crange(a[0][0], a[0][1]):
		for j in crange(a[1][0], a[1][1]):
			for k in crange(a[2][0], a[2][1]):
				cubes[i-min_c][j-min_c][k-min_c] = val


print(cubes)
print(sum(sum(sum(y) for y in x) for x in cubes))
