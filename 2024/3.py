from util import *

ll = readlines("3.in")

def f(s):
    m = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", s)
    m = [(int(x), int(y)) for x, y in m]
    return sum([x*y for x,y in m])

#p1
s=0
for l in ll:
    s += f(l)

print(s)

#p2
s= 0
l = "do()"+ (" ").join(ll)
for p in l.split("don't()"):
    a = p.split("do()", 1)
    if len(a) == 1: continue
    s += f(a[1])
print(s)