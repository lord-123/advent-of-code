with open("input" , "r") as file:
	lines = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in file.readlines()]

MAX_COORD = 1000
map = [[0 for i in range(MAX_COORD)] for i in range(MAX_COORD)]


for i in lines:
	# matching x
	if i[0][0] == i[1][0]:
		x = i[0][0]
		y1 = i[0][1]
		y2 = i[1][1]

		y=y1
		while y != y2 + (1 if y2>y1 else -1):
			map[x][y] += 1
			if y1 < y2:
				y+=1
			else:
				y-=1

	# matching y
	elif i[0][1] == i[1][1]:
		y = i[0][1]
		x1 = i[0][0]
		x2 = i[1][0]

		x=x1
		while x != x2 + (1 if x2>x1 else -1):
			map[x][y] += 1
			if x1 < x2:
				x+=1
			else:
				x-=1
	
	else:
		x1 = i[0][0]
		x2 = i[1][0]

		y1 = i[0][1]
		y2 = i[1][1]

		x = x1
		y = y1

		while x != x2 + (1 if x2>x1 else -1):
			map[x][y] += 1
			if x1<x2:
				x+=1
			else:
				x-=1

			if y1<y2:
				y+=1
			else:
				y-=1
			
#for x in map:
#	print(x)

print(sum(sum(y >= 2 for y in x) for x in map))
