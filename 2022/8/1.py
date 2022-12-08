with open("input") as f:
	t = [list(map(int,x)) for x in f.read().split("\n")[:-1]]

print(t)

c = (len(t) * len(t[0])) - ((len(t)-2) * (len(t[0])-2))

#p1
for i in range(1, len(t)-1):
	for j in range(1, len(t[0])-1):
		if max(t[i][:j]) < t[i][j]:
			c+=1
		elif max(t[i][j+1:]) < t[i][j]:
			c+=1
		elif max([t[l][j] for l in range(i)]) < t[i][j]:
			c+=1
		elif max([t[l][j] for l in range(i+1, len(t))]) < t[i][j]:
			c+=1

print(c)

#p2
scores = []
for i in range(1, len(t)-1):
	for j in range(1, len(t[0])-1):
		left = 0
		for x in t[i][:j][::-1]:
			left += 1
			if x >= t[i][j]: break
		right = 0
		for x in t[i][j+1:]:
			right += 1
			if x >= t[i][j]: break
		top = 0
		for x in [t[l][j] for l in range(i)][::-1]:
			top += 1
			if x >= t[i][j]: break
		bottom = 0
		for x in [t[l][j] for l in range(i+1, len(t))]:
			bottom += 1
			if x >= t[i][j]: break
		scores += [left*right*top*bottom]

print(max(scores))
