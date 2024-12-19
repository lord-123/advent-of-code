from util import *
from functools import cache

patterns, _, *designs = readlines("19.in")
patterns = tuple(patterns.split(", "))

@cache
def ismatch(design, patterns):
    if len(design) == 0: return 1

    c = 0
    for p in patterns:
        if design.startswith(p):
            c += ismatch(design[len(p):], patterns)

    return c

print(sum([ismatch(d, patterns) > 0 for d in designs]))
print(sum([ismatch(d, patterns) for d in designs]))