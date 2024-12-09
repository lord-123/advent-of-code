from util import *
from scipy.ndimage import rotate

ll = readlines("4.in")
n = len(ll)
m = len(ll[0])

# p1

g = [lambda x,y:x, lambda x,y:y, lambda x,y:x+y, lambda x,y:x-y]
s = 0
for f in g:
    r = groups(ll, f)
    #print(["".join(x) for x in r])
    k = lmap(lambda x: len(re.findall(r"(?=(XMAS|SAMX))", "".join(x))), r)
    s += sum(k)
print(s)

# p2

A = []
for i, l in enumerate(ll):
    for j, x in enumerate(l):
        if x == "A":
            A += [(i,j)]

def isxmas(x):
    i,j=x
    if i < 1 or j < 1:
        return False
    if i >= n-1 or j >= m-1:
        return False
    
    d1 = set([ll[i-1][j-1], ll[i+1][j+1]])
    d2 = set([ll[i-1][j+1], ll[i+1][j-1]])
    expected = set("MS")

    if d1 != expected or d2 != expected:
        return False
    
    return True

s = sum(map(isxmas, A))

print(s)
