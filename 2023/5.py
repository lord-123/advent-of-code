from util import *

fname = "input5"
#fname = "example5"

ll = readlines(fname)
s = readstanzas(fname)
#print(s)

seeds = tmap(int, s[0][0].split(": ")[1].split())
#print(seeds)

s = s[1:]
maps = {}
for x in s:
    key = tuple(x[0].split()[0].split("-to-"))
    key = x[0].split()[0].split("-to-")[0]
    m = []
    for l in x[1:]:
        m+= [tmap(int, l.split())]
    maps[key]= m

print(maps)

def find(m, i):
    for x in m:
        dest, src, ln = x
        if src <= i and i <= src + ln - 1:
            return dest + (i-src)
    return i

cats = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

locations = []
for x in seeds:
    n = x
    for key in cats[:-1]:
        n = find(maps[key], n)
    locations += [n]

print(locations)
p1 = min(locations)
print(f"p1: {p1}")

### p2

seeds = list(zip(*(iter(seeds),) * 2))
seeds = [(a, a+b) for a,b in seeds]
print(seeds)

def r_sub(r1, r2):
    s1, e1 = r1
    s2, e2 = r2
    if s2 > s1 and e2 < e1:
        return [[s1, s2-1], [e2+1, e1]]
    if s2 > s1 and e2 >= e1:
        return [[s1, s2-1]]
    if s2 <= s1 and e2 < e1:
        return [[e2+1, e1]]
    if s2 <= s1 and e2 >= e1:
        return []
    return []

#print(r_sub([79,95],[72,88]))
#exit()

def convert_range(m, r):
    #print(r)
    #print("m", m)
    k = [r]
    new = []
    start, end = r
    for x in m:
        dest,src,ln = x
        src_s = src
        src_e = src+ln
        if not (start <= src_e and src_s <= end): continue
        trans = src-dest
        new += [[max(src_s, start)-trans, min(src_e, end)-trans]]
        k = flat(map(lambda a: r_sub(a, [src_s, src_e]), k))

    #print("nk", new,k)
    return merge(new+k)

#print(convert_range([(50, 98, 2), (52, 50, 48)], [79, 99]))

#exit()
r = []
for x in seeds:
    ranges = [list(x)]
    for key in cats[:-1]:
        ranges = merge(flat([convert_range(maps[key], n) for n in ranges]))
    r += ranges

print(r)

p2 = min(x[0] for x in r)
print(f"p2: {p2}")
