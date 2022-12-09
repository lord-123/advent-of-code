with open("input", "r") as f:
	m = [x.split(" ") for x in f.read().split("\n")[:-1]]
	m = list(map(lambda x: [x[0], int(x[1])], m))

h = [0,0]
t = [0,0]

pos = set()

#p1
def move(d):
	if d == "R":
		h[0] += 1
	elif d == "U":
		h[1] += 1
	elif d == "L":
		h[0] -= 1
	elif d == "D":
		h[1] -= 1
	
	if t[0] == h[0]-2:
		t[0] += 1
		t[1] = h[1]
	elif t[0] == h[0]+2:
		t[0] -= 1
		t[1] = h[1]
	elif t[1] == h[1]-2:
		t[1] += 1
		t[0] = h[0]
	elif t[1] == h[1]+2:
		t[1] -= 1
		t[0] = h[0]
	
	pos.add(tuple(t))

for x in m:
	for i in range(x[1]):
		move(x[0])

print(m)
print(pos)
print(len(pos))

#p2
pos = set()
r = [[0,0] for x in range(10)]
def move2(d):
	if d == "R":
		r[0][0] += 1
	elif d == "U":
		r[0][1] += 1
	elif d == "L":
		r[0][0] -= 1
	elif d == "D":
		r[0][1] -= 1
	
	for i in range(1, len(r)):
		if r[i][0] == r[i-1][0]-2 and r[i][1] == r[i-1][1]-2:
			r[i][0] += 1
			r[i][1] += 1
		elif r[i][0] == r[i-1][0]-2 and r[i][1] == r[i-1][1]+2:
			r[i][0] += 1
			r[i][1] -= 1
		elif r[i][0] == r[i-1][0]+2 and r[i][1] == r[i-1][1]-2:
			r[i][0] -= 1
			r[i][1] += 1
		elif r[i][0] == r[i-1][0]+2 and r[i][1] == r[i-1][1]+2:
			r[i][0] -= 1
			r[i][1] -= 1
		elif r[i][0] == r[i-1][0]-2:
			r[i][0] += 1
			r[i][1] = r[i-1][1]
		elif r[i][0] == r[i-1][0]+2:
			r[i][0] -= 1
			r[i][1] = r[i-1][1]
		elif r[i][1] == r[i-1][1]-2:
			r[i][1] += 1
			r[i][0] = r[i-1][0]
		elif r[i][1] == r[i-1][1]+2:
			r[i][1] -= 1
			r[i][0] = r[i-1][0]
	
	print(r)
	pos.add(tuple(r[-1]))

for x in m:
	for i in range(x[1]):
		move2(x[0])

print("p2")
print(r)
print(pos)
print(len(pos))
