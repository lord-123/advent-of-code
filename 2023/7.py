from util import *
from collections import Counter

fname = "input7"
#fname = "example7"

ll = readlines(fname)
h = tmap(lambda x: x.split(), ll)
#print(h)

types = {
    100: lambda x: max(Counter(x).values()) == 5,
    90: lambda x: max(Counter(x).values()) == 4,
    80: lambda x: set(Counter(x).values()) == {2,3},
    70: lambda x: max(Counter(x).values()) == 3,
    60: lambda x: sorted(Counter(x).values()) == [1,2,2],
    50: lambda x: sorted(Counter(x).values()) == [1,1,1,2],
    40: lambda x: max(Counter(x).values()) == 1
}

def score(hand):
    for t in types:
        if types[t](hand): return t
    print(f"FAILED: {hand}")
    return None

def mutate(hand):
    return lmap(lambda x: "23456789TJQKA".find(x), hand)

ranked = (sorted(h, key=lambda x:[score(x[0])]+mutate(x[0])))
print(ranked)

p1 = 0
for i,x in enumerate(ranked, 1):
    p1 += i * int(x[1])

print(f"p1: {p1}")

# p2
def mutate2(hand):
    return lmap(lambda x: "J23456789TQKA".find(x), hand)

def score2(hand):
    return max(score(x) for x in [hand.replace("J", c) for c in "23456789TQKA"])
ranked = (sorted(h, key=lambda x:[score2(x[0])]+mutate2(x[0])))

p2 = 0
for i,x in enumerate(ranked, 1):
    p2 += i * int(x[1])

print(f"p2: {p2}")
