from util import *
from z3 import *

s = readstanzas("13.in")

b = []
for x in s:
    b += [{
        "A": ints(x[0]),
        "B": ints(x[1]),
        "p": list(ints(x[2]))
    }]

#print(b)

def cost(machine):
    A, B = Ints("A B")
    o = Optimize()

    o.add(A >= 0, B >= 0)
    o.add(A * machine["A"][0] + B * machine["B"][0] == machine["p"][0])
    o.add(A * machine["A"][1] + B * machine["B"][1] == machine["p"][1])
    o.minimize(A*3 + B)
    if o.check() == sat:
        return o.model().eval(A*3 + B).as_long()
    return 0

print(sum(cost(x) for x in b))

for i in range(len(b)):
    b[i]["p"][0] += 10000000000000
    b[i]["p"][1] += 10000000000000

print(sum(cost(x) for x in b))