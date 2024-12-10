from util import *

map = lmap(int, read("9.in"))

print(map)

FILE = 0
SPACE = 1

mode = FILE

files = [x for i, x in enumerate(map) if i%2 == 0]
spaces = [x for i, x in enumerate(map) if i%2 == 1]

print(files, spaces)

end = len(files)-1
position = 0
fp = 0
sp = 0
s = 0
while fp < end:
    # do the file
    for _ in range(files[fp]):
        s += position * fp
        position += 1

    # do the space
    if fp >= len(spaces): continue

    gap = spaces[fp]
    while gap > 0:
        if files[end] > gap:
            files[end] -= gap
            for _ in range(gap):
                s += position * end
                position += 1
            gap = 0
        elif files[end] == gap:
            for _ in range(gap):
                s += position * end
                position += 1
            gap = 0
            end -= 1
        else:
            c = files[end]
            for _ in range(c):
                s += position * end
                position += 1
            end -= 1
            gap -= c

    #print(s)
    fp += 1

for _ in range(files[fp]):
    s += position * fp

# p1
print(s)

s = 0
fp = 0
end = len(files) - 1
position = 0
files = [[False, x] for i, x in enumerate(map) if i%2 == 0]
spaces = [x for i, x in enumerate(map) if i%2 == 1]

#print(files)
while fp < end:
    #do file
    used, length = files[fp]
    if not used:
        for _ in range(length):
            s += position * fp
            #print(position, fp)
            position += 1
    else:
        position += length
    #do space
    gap = spaces[fp]
    e = end
    while e > fp:
        used, length = files[e]
        if length <= gap and not used:
            #print(length, gap, e)
            for _ in range(length):
                s += position * e
                #print(position, e)
                position += 1
            gap -= length
            files[e][0] = True
        e -= 1
        #print(e)
    position += gap
    fp += 1

print(s)