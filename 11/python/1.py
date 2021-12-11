a = "input"
with open(a, "r") as file:
	o = [[int(x) for x in y.strip("\n")] for y in file.readlines()]

def printO():
	for x in o:
		print(x)

cur_flashed=[]
def flash(i, j):
	global cur_flashed
	if (i, j) not in cur_flashed:
		cur_flashed += [(i, j)]
		o[i][j] = 0
		flashed(i-1, j-1)
		flashed(i-1, j)
		flashed(i-1, j+1)
		flashed(i, j-1)
		flashed(i, j+1)
		flashed(i+1, j-1)
		flashed(i+1, j)
		flashed(i+1, j+1)


def flashed(i, j):
	if i < 0 or j < 0 or i > len(o) - 1 or j > len(o[0]) - 1:
		return
	if (i, j) in cur_flashed:
		return
	o[i][j] += 1
	if o[i][j] > 9:
		flash(i, j)

total_flashed = 0
c = 0
while True:
	cur_flashed = []
	o = [[x + 1 for x in y] for y in o]

	for i in range(len(o)):
		for j in range(len(o[0])):
			if o[i][j] > 9:
				flash(i, j)
	
	c+=1

	total_flashed += len(cur_flashed)
	printO()
	print(cur_flashed)

	if len(cur_flashed) == len(o) * len(o[0]):
		break

print(c)
