with open("input", "r") as file:
	area = [[int(y) for y in x.split("..")] for x in file.read()[15:].split(", y=")]

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

