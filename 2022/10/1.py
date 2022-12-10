with open("input", "r") as f:
	c = [x.split(" ") for x in f.read().split("\n")]

x = 1
ticks = [x]
for i in c:
	if i[0] == "addx":
		ticks += [x]
		x += int(i[1])
	ticks+=[x]

print(x)
print(ticks)
print(sum((i+1) * x for i, x in list(enumerate(ticks))[19::40]))

#p2
crt = ["" for i in range(6)]
cycle = 1
x = 1
for i in c:
	if cycle >= 240: break
	row = (cycle-1)//40
	column = cycle%40-1
	crt[row] += "#" if column >= x-1 and column <= x+1 else "."

	if i[0] == "addx":
		cycle+=1
		row = (cycle-1)//40
		column = cycle%40-1
		crt[row] += "#" if column >= x-1 and column <= x+1 else "."
		x += int(i[1])
	
	cycle+=1

for i in crt:
	print(i)
