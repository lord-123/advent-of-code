with open("input") as f:
	p = [list(map(lambda k: list(map(int, k.split("-"))), y)) for y in [x.strip().split(",") for x in f.readlines()]]

c = 0
# p1
for x in p:
	if x[0][0] <= x[1][0] and x[0][1] >= x[1][1]:
		c += 1
	elif x[1][0] <= x[0][0] and x[1][1] >= x[0][1]:
		c += 1

print(p)
print(c)

#p2
c=0
for x in p:
	if x[0][0] <= x[1][1] and x[1][0] <= x[0][1]:
		c+=1

print(c)
