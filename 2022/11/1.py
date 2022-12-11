with open("input", "r") as f:
	m = [x.split("\n") for x in f.read().split("\n\n")]

print(m)

def createLambda(s):
	return lambda old: eval(s)

monkeys = []
mod = 1
for x in m:
	monkeys += [{
			"items": list(map(int, x[1][18:].split(", "))),
			"op": createLambda(x[2][19:]),
			"test": int(x[3][21:]),
			"true": int(x[4][29:]),
			"false": int(x[5][30:]),
			"throws": 0
	}]
	mod *= monkeys[-1]["test"]

print(monkeys)

def round():
	global monkeys
	for i, m in enumerate(monkeys):
		while len(m["items"]) > 0:
			i = m["op"](m["items"].pop(0))%mod
			if i % m["test"] == 0:
				monkeys[m["true"]]["items"] += [i]
			else:
				monkeys[m["false"]]["items"] += [i]
			m["throws"] += 1

for i in range(10000):
	print(i)
	round()
print(monkeys)
throws = sorted([m["throws"] for m in monkeys])
print(throws)
print(throws[-2] * throws[-1])
