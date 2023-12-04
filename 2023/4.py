from util import *

fname = "input4"
#fname = "example4"

ll = readlines(fname)

p1 = 0
cardc = [1 for x in range(len(ll))]
for i,l in enumerate(ll):
    l = l.split(": ")[1]
    winners, owned = [tmap(int, x.split()) for x in l.split(" | ")]

    c = 0
    for x in owned:
        if x in winners:
            c += 1
    for j in range(c):
        if i+j+1 >= len(ll): break
        cardc[i+j+1] += cardc[i]
    if c != 0:
        p1+= 2**(c-1)

p2 = sum(cardc)
print(cardc)

print(f"p1: {p1}")
print(f"p2: {p2}")
