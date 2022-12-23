import re

with open("input", "r") as file:
	maze, instructions = file.read()[:-1].split("\n\n")

DIRS = (
	( 1,  0),
	( 0,  1),
	(-1,  0),
	( 0, -1))

maze = [[len(x) - len(x.lstrip()), x.strip()] for x in maze.split("\n")]
maze += [[0, ""]]
for x in maze:
	x[0] = int(x[0])
instructions = re.split("([LR])", instructions)

print(maze)
print(instructions)

# p1
"""
def get_next(pos, facing):
	if DIRS[facing][1] == 0:
		return ((pos[0] + DIRS[facing][0]) % len(maze[pos[1]][1]), pos[1])

	newy = pos[1] + DIRS[facing][1]
	if not (pos[0] + maze[pos[1]][0] >= maze[newy][0] and pos[0] + maze[pos[1]][0] <= maze[newy][0] + len(maze[newy][1])):
		newy -= 2*DIRS[facing][1]
		while pos[0] + maze[pos[1]][0] > maze[newy][0] and pos[0] + maze[pos[1]][0] < maze[newy][0] + len(maze[newy][1]):
			newy -= DIRS[facing][1]

		newy += DIRS[facing][1]

	newx = pos[0] + maze[pos[1]][0] - maze[newy][0]
	return (newx, newy)
"""
# p2
"""
 BA
 C
ED
F
"""
def print_maze():
	for pad, x in maze:
		print(" "*pad + x)
def get_next(pos, facing):
	x, y = pos
	xd, yd = DIRS[facing]

	# hardcode bc fuck that


	newx = x+xd
	newy = y+yd
	if len(maze) > newy and newy >= 0:
		newx = newx - maze[newy][0] + maze[y][0]

		if newx >= 0 and newx < len(maze[newy][1]):
			return (newx, newy, facing)
	
	x = newx
	y = newy
	match facing, x//50, y//50:
		case 0, 0, _: return 149-x, 99, 2
		case 0, 1, _: return 49, x+50, 1
		case 0, 2, _: return 149-x, 149, 2
		case 0, 3, _: return 149, x-100, 2
		case 2, 0, _: return 149-x, 0, 0
		case 2, 1, _: return 100, x-50, 3
		case 2, 2, _: return 149-x, 50, 0
		case 2, 3, _: return 0, x-100, 3
		case 3, _, 0: return 0, y+100, 3
		case 3, _, 1: return 100+y, 49, 2
		case 3, _, 2: return 50-y, 99, 2
		case 1, _, 0: return 50+y, 50, 0
		case 1, _, 1: return 100+y, 0, 0
		case 1, _, 2: return 199, y-100, 1
	print("fucked it")
	print(x, y, facing)
	return
	# B-E
	if x == 0 and y < 50 and facing == 2:
		return (0, y+100, 0)
	# B-F
	elif x < 50 and y == 0 and facing == 3:
		return (0, x+150, 0)
	# A-C
	elif x >= 50 and y == 49 and facing == 1:
		return (49, x, 3)
	# A-F
	elif x >= 50 and y == 0 and facing == 3:
		return(x-50, 199, 3)
	# A-D
	elif x == 99 and y < 50 and facing == 0:
		return (99, 100+(49-y), 2)
	# C-A
	elif x == 49 and y < 100 and y > 49 and facing == 0:
		return (50+y-50, 49, 3)
	# C-E
	elif x ==0 and y < 100 and y > 49 and facing == 2:
		return (y-50 , 100, 1)
	# D-A
	elif x == 99 and y < 150 and y > 99 and facing == 0:
		return (99, 149-y, 2)
	elif x > 49 and y == 149 and facing == 1:
		return (49, 150+x-50, 2)
	# E-B
	elif x == 0 and y < 150 and y > 99 and facing == 2:
		return (0, 49-(y-100), 0)
	elif x < 50 and y == 100 and facing == 3:
		return (0, 50+x, 0)
	# F-A
	elif y == 199 and facing == 1:
		return (x+50, 0, 1)
	elif x == 0 and y > 149 and facing == 2:
		return (y-150, 0, 1)
	elif x == 49 and y > 149 and facing == 0:
		return (50+y-150, 149, 3)
	else:
		print_maze()
		print("fucked it")
		print(x, y, facing)

def maze_idx(x, y):
	return maze[y][1][x]

def set_maze(x, y, c):
	l = list(maze[y][1])
	l[x] = c
	maze[y][1] = "".join(l)

print(get_next([99, 0], 0), "99 149 2")
print(get_next([99, 0], 3), "49 199 3")
print(get_next([99, 49], 1), "49 99 3")
print(get_next([99, 0], 0), "99 149 2")
print(get_next([99, 0], 0), "99 149 2")
print(get_next([99, 0], 0), "99 149 2")

pos = [0, 0]
facing = 0
set_maze(0, 0, ">")
arrows = [">", "v", "<", "^"]
for j, x in enumerate(instructions):
	#print(x)
	if x == "R":
		facing += 1
		facing %= len(DIRS)
		continue
	if x == "L":
		facing -= 1
		facing %= len(DIRS)
		continue

	for i in range(int(x)):
		set_maze(*pos, arrows[facing])
		x, y, facing = get_next(pos, facing)
		n = (x,y)
		if maze_idx(*n) == "#": break
		pos = list(n)

print_maze()
print(pos[0]+1+maze[pos[1]][0], pos[1]+1, facing)
print(sum([(pos[0]+1+maze[pos[1]][0])*4, (pos[1]+1)*1000, facing]))

