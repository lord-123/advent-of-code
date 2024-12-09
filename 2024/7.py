from util import *

ll = readlinesints("7.in")

def possible(x, l, s=0):
    if len(l) == 0:
        return x==s
    
    rest = l[1:]
    return possible(x, rest, s+l[0]) or possible(x, rest, s*l[0])

s = 0
for x, f, *l in ll:
    if possible(x, l, f):
        s += x

# p1
print(s)

def possible2(x, l, s=0):
    if len(l) == 0:
        return x==s
    
    rest = l[1:]
    return possible2(x, rest, s+l[0]) or possible2(x, rest, s*l[0]) or possible2(x, rest, int(str(s) + str(l[0])))

s = 0
for x, f, *l in ll:
    if possible2(x, l, f):
        s += x

#print([possible2(x, l, f) for x, f, *l in ll])

print(s)