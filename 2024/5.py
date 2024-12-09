from util import *

r, u = readstanzas("5.in")

r = tmap(ints, r)
u = tmap(ints, u)

# print(r)
# print(u)

rules = defaultdict(list)

for a, b in r:
    rules[a] += [b]

#print(rules)

def find_error(update):
    for i, x in enumerate(update):
        for a in rules[x]:
            try:
                j = update.index(a, 0, i)
                return (i, j)
            except:
                pass
            
    return None

def valid(update):
    return find_error(update) is None

#p1
print(sum([x[len(x)//2] for x in u if valid(x)]))

def correct(update):
    update = list(update)
    while (e:=find_error(update)) is not None:
        i,j = e
        t = update[i]
        update[i] = update[j]
        update[j] = t
    return update

# p2
#c = [correct(x) for x in u if not valid(x)]
#print(c)
print(sum(correct(x)[len(x)//2] for x in u if not valid(x)))