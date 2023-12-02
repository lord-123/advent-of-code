from util import *
fname = "input2"
#fname = "example2"

lines = readlines(fname)

games = []

for i,l in enumerate(lines, 1):
    games += [[{y[1]: int(y[0]) for y in lmap(lambda k: k.split(" "), x.split(", "))} for x in l[7+len(str(i)):].split("; ")]]

#print(games)

p1 = 0
for i,g in enumerate(games,1):
    ok = True
    for s in g:
        if "red" in s:
            if s["red"] > 12: ok = False; break
        if "green" in s:
            if s["green"] > 13: ok = False; break
        if "blue" in s:
            if s["blue"] > 14: ok = False; break
    if ok:
        p1 += i
        #print(i)

print("p1:", p1)

p2 = 0
for g in games:
    maxs = defaultdict(lambda: 0)
    for s in g:
        for k in s:
            maxs[k] = max(maxs[k], s[k])
    power = 1
    for k in maxs:
        power *= maxs[k]
    p2 += power

print("p2:", p2)
