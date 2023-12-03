from util import *
fname = "input3"
#fname = "example3"


lines = readlines(fname)

nums = []

surrounding = defaultdict(list)
for l in lines:
    i = 0
    ran = [0,0]
    ranges = {}
    reading = False
    for j,x in enumerate(l):
        if x in "0123456789":
            if not reading:
                ran[0] = j
            reading = True
            i *= 10
            i += int(x)
            ran[1] = j
        else:
            if reading:
                reading=False
                ranges[tuple(ran)]=i
                ran[0] = j+1
                i = 0
    if reading:
        reading=False
        ranges[tuple(ran)]=i
        ran[0] = j+1
        i = 0
    nums += [ranges]

def around(p):
    for d in ALL_DIRS:
        yield (p[0]+d[0],p[1]+d[1])

p1 = 0
l = []
for i,ranges in enumerate(nums):
    for r in ranges:
        done = False
        for x in range(r[0]-1, r[1]+2):
            if done: break
            for y in range(i-1, i+2):
                surrounding[x,y]+=[nums[i][r]]
                if y < 0 or y > len(lines)-1 or x < 0 or x > len(lines[0]) -1: continue
                if lines[y][x] not in "0123456789.":
                    p1+= nums[i][r]
                    l += [nums[i][r]]
                    #print(nums[i][r])
                    done = True
                    break
            #if any([lines[y][x] not in "0123456789." for y,x in around([i,k]) if y > -1 and y < len(lines) and x > -1 and x < len(lines[0])]):
                   #p1 += nums[i][r]
                   #break


#print(l)
print("p1:", p1)

p2=0
for i,l in enumerate(lines):
    for j,c in enumerate(l):
        if c == "*":
            g = surrounding[j,i]
            if len(g)==1: continue
            p = 1
            for x in g: p *= x
            p2 += p

print("p2:", p2)
