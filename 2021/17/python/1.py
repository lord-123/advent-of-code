with open("input", "r") as file:
	area = [[int(y) for y in x.split("..")] for x in file.read()[15:].split(", y=")]

with open("comparison", "r") as file:
	comparison = [tuple(int(y) for y in x.split(",")) for x in file.read().split(" ")]

print(area)

n = 0
while True:
	x = (n*(n+1))//2
	if area[0][0] <= x and x <= area[0][1]:
		break
	n +=1


y = -(min(area[1])+1)
print(x, y)
print((y*(y+1))//2)
min_x = n

x_positions = []
for x in range(min_x, area[0][1]+1):
	for i in range(x, -1, -1):
		location = (x*(x+1))//2 - (i*(i+1))//2
		if area[0][0] <= location and location <= area[0][1]:
			x_positions += [(x, x-i)]
			if i == 0:
				for j in range(1,1000):
					x_positions += [(x, x+j)]
		if location > area[0][1]:
			break
		
print(x_positions)

y_positions = []
for y in range(area[1][0], -(area[1][0])+1):
	pos = y
	i = 1
	while True:
		if area[1][0] <= pos and pos <= area[1][1]:
			y_positions += [(y, i)]
		if pos < area[1][0]:
			break
		pos += y-i
		i += 1

print(y_positions)

positions = {(x[0], y[0]) for x in x_positions for y in y_positions if x[1]==y[1]}
print(positions)
print(len(positions))
#print(comparison)
#print(len(comparison))

#for x in positions:
#	if x not in comparison:
#		print(f"{x} not in comparison")
#for x in comparison:
#	if x not in positions:
#		print(f"{x} not in positions")
