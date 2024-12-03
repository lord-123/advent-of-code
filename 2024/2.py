from util import *

levels = readlinesints("2.in")

def safe(level):
    monotonic = all(x<=y for x,y in zip(level, level[1:])) or \
                all(x>=y for x,y in zip(level, level[1:]))
    
    if not monotonic: return False

    return all(1<=abs(x-y) and abs(x-y)<=3 for x,y in zip(level, level[1:]))

c = sum(map(safe, levels))

print(c)


def safe2(level):
    return any(safe(level[:i]+level[i+1:]) for i in range(len(level)))
        


print(sum(map(safe2, levels)))