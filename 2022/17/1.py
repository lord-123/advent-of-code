#probably only works properly for part 2 now
#also fails on the given example
from collections import defaultdict
with open("input", "r") as f:
	jets = f.read()[:-1]

rocks = [
	[[1,1,1,1]],
	[[0,1,0],[1,1,1],[0,1,0]],
	[[0,0,1],[0,0,1],[1,1,1]],
	[[1],[1],[1],[1]],
	[[1,1],[1,1]]
]

chamber = defaultdict(lambda: [0,0,0,0,0,0,0])
chamber[0] = [1,1,1,1,1,1,1]
pheight = 0
pdiff = 0
height = 0
jetsi = 0

def simrock(rocki):
	global height, chamber, jetsi, pheight, pdiff

pheight=0
last=[[[1,1,1,1,1,1,1], 0]]
calc = 1000000000000
count_to = 1000000000000
rocki = 0
prock = 0
prockdiff=0
debug = False
save = 0
for rocki in range(calc):
	count_to -= 1
	if count_to == 0: break
	r = rocks[rocki%len(rocks)]
	# position of top left of rock
	y = height + 3 + len(r)
	x = 2
	landed = False
	while not landed:
		leftblock = False
		rightblock = False
		for i, a in enumerate(r):
			for j, b in enumerate(a):
				if b == 1:
					if x+j-1 >= 0:
						if chamber[y-i][x+j-1] == 1:
							leftblock = True
					if x+j+1 < 7:
						if chamber[y-i][x+j+1] == 1:
							rightblock = True
		#print(x, y, leftblock, rightblock)
		if jetsi == 0 and rocki > 0:
			diff = height-pheight
			rockdiff = rocki-prock
			print(f"rock: {rocki} rockdiff: {rockdiff} pheight: {pheight} height: {height} diff: {diff}")
			if diff == pdiff and diff != 0:
				count_to = (calc - rocki) % (rockdiff)
				print(f"found cycle {count_to}")
				save = ((calc-rocki)//rockdiff)*diff
				rocki = 0
			
			prockdiff=rocki-prock
			prock = rocki
			pheight = height
			pdiff = diff

		if jets[jetsi] == "<" and x > 0 and not leftblock:
			x -=1
		elif jets[jetsi] == ">" and x + len(r[0]) < 7 and not rightblock:
			x += 1
		jetsi+=1
		jetsi = jetsi % len(jets)

		for i, a in enumerate(r):
			for j, b in enumerate(a):
				if b == 1:
					#print(y-i, x+j)
					if chamber[y-i-1][x+j] == 1:
						#print("landing", x, y)
						landed = True
						break
		if not landed: y-=1
	
	#write in position
	for i, a in enumerate(r):
		for j, b in enumerate(a):
			chamber[y-i][x+j] |= b

	height = max(height, y)
	#print(height)

	if debug:
		print(i, jetsi)
		for j in range(height+1):
			print("".join(["#" if x == 1 else " " for x in chamber[height-j]]))

	rocki += 1

print(height, save)
print(height + save)

"""
for j in range(height+1):
	print("".join(["#" if x == 1 else " " for x in chamber[height-j]]))
"""
