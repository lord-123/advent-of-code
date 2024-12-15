from util import *

ma, moves = readstanzas("15.in")
n = len(ma)
m = len(ma[0])

moves = "".join(moves)

walls = set()
boxes = set()

for i, l in enumerate(ma):
    for j, c in enumerate(l):
        if c == "#":
            walls.add((i,j))
        elif c == "O":
            boxes.add((i,j))
        elif c == "@":
            robot = (i,j)

def movebox(b, v):
    n = (b[0]+v[0], b[1]+v[1])
    if n in walls:
        return False
    elif n in boxes:
        if not movebox(n, v):
            return False
    boxes.remove(b)
    boxes.add(n)
    return True

def move(dir):
    global robot
    v = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0)
    }[dir]

    n = (robot[0]+v[0], robot[1]+v[1])
    if n in walls:
        return False
    elif n in boxes:
        if not movebox(n, v):
            return False
    robot = n
    return True

def drawstate():
    s = ""
    for i in range(n):
        for j in range(m):
            if (i,j) in walls: s += "#"
            elif (i,j) in boxes: s += "["
            elif (i, j-1) in boxes: s+= "]"
            elif (i,j) == robot: s+= "@"
            else: s += "."
        s += "\n"
    print(s)

for c in moves:
    move(c)

# p1
print(sum(b[0]*100 + b[1] for b in boxes))

m *= 2
walls = set()
boxes = set()

for i, l in enumerate(ma):
    for j, c in enumerate(l):
        if c == "#":
            walls.add((i,j*2))
            walls.add((i, j*2+1))
        elif c == "O":
            boxes.add((i,j*2))
        elif c == "@":
            robot = (i,j*2)

def canmovebox(b, v):
    horizontal = v[0] == 0
    n = (b[0]+v[0], b[1]+v[1])
    tomove = set([b])
    if not horizontal:
        if n in walls or (n[0], n[1]+1) in walls:
            return False
        for i in (-1,0,1):
            x = (n[0], n[1]+i)
            if x in boxes:
                k = canmovebox(x, v)
                if k == False:
                    return False
                else:
                    tomove.update(k)
    else:
        m= (n[0]+v[0], n[1]+v[1])
        if v[1] == -1:
            if n in walls:
                return False
        else: 
            if m in walls:
                return False
        if m in boxes:
            k = canmovebox(m, v)
            if k == False:
                return False
            else:
                tomove.update(k)
    return tomove

def movebox(b, v):
    k = canmovebox(b, v)
    if k == False:
        return False
    else:
        for x in k:
            boxes.remove(x)
            boxes.add((x[0]+v[0], x[1]+v[1]))
        return True

def move(dir):
    global robot
    v = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0)
    }[dir]

    tomove = set()

    horizontal = dir in "<>"
    n = (robot[0]+v[0], robot[1]+v[1])
    if not horizontal:
        if n in walls:
            return False
        for i in (-1,0):
            x = (n[0], n[1]+i)
            if x in boxes:
                k = canmovebox(x, v)
                if k == False:
                    return False
                else:
                    tomove.update(k)
    else:
        if n in walls:
            return False
        if n in boxes:
            k = canmovebox(n, v)
            if k == False:
                return False
            else:
                tomove.update(k)
        m= (n[0], n[1]-1)
        if m in boxes:
            k = canmovebox(m, v)
            if k == False:
                return False
            else:
                tomove.update(k)
    #print(tomove)
    for x in tomove:
        boxes.remove(x)
    for x in tomove:
        boxes.add((x[0]+v[0], x[1]+v[1]))
        
    robot = n
    return True

#print((1,10) in walls)

for c in moves:
    move(c)

    #print(c)
    #drawstate()
    #input()
print(sum(b[0]*100 + b[1] for b in boxes))