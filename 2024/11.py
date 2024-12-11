from util import *
from functools import cache

stones = ints(read("11.in"))

print(stones)

def next(x):
    if x == 0: return (1,)
    s = str(x)
    n = len(s)
    if n%2 == 0: return tmap(int, (s[:n//2], s[n//2:]))
    else: return (x*2024,)

@cache
def count(x, n=25):
    if n == 0: return 0
    f = next(x)
    return sum(count(v, n-1) for v in f) + len(f) - 1

# p1
print(sum([count(x) for x in stones]) + len(stones))

# p2
print(sum([count(x, 75) for x in stones]) + len(stones))