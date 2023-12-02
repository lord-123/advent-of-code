from functools import cache
with open("input", "r") as file:
	ll = file.read()[:-1].split("\n")

blizzards = [ ((x,y), v) for y,l in enumerate(ll) for x,v in enumerate(l) if v in "^>v<" ]
minx = 1
miny = 1
maxx = len(ll[0])-2
maxy = len(ll)-2
target = (maxx, maxy+1)

"""
def move(b):
	new = []
	for p in b:
		pos,d = p
		x,y = pos
		if d == "^":
			y-=1
		if d == "v":
			y+=1
		if d == ">":
			x+=1
		if d == "<":
			x-=1

		if x < minx: x = maxx
		if x > maxx: x = minx
		if y < miny: y = maxy
		if y > maxy: y = miny

		new += [((x,y), d)]
	return new
"""
@cache
def get_blizzard(time):
	newb = set()
	for b in blizzards:
		x,y = b[0]
		d = b[1]
		
		if d == "^": y -= time
		if d == "v": y += time
		if d == ">": x += time
		if d == "<": x -= time

		x = minx + (x-1)%maxx
		y = miny + (y-1)%maxy

		newb.add((x,y))

	return newb

def get_neighbours(pos, time, tgt):
	n = []
	b = get_blizzard(time)
	for x,y in [(-1,0),(1,0),(0,-1),(0,1),(0,0)]:
		newpos = (pos[0]+x, pos[1]+y)
		if newpos == tgt: return [tgt]
		if (newpos[0] < minx or newpos[0] > maxx or newpos[1] < miny or newpos[1] > maxy) and newpos != (1,0) and newpos != target:
			continue
		
		if newpos not in b:
			n += [newpos]
	return n

def find(src, tgt, start=0):
	q = [(src, start)]
	seen = set()
	i = 0
	while len(q) > 0:
		v,t = q.pop(0)
		#print(v)
		if v == tgt:
			return t
		if (v,t) in seen: continue
		seen.add((v,t))

		for n in get_neighbours(v, t+1, tgt):
			q += [(n, t+1)]
		i+=1

ans = find((1,0), target)
print("p1", ans)

t2 = find(target, (1,0), ans)
#print("t2", t2)
t3 = find((1,0), target, t2)

print("p2", t3)
