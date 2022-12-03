with open("input", "r") as f:
	l = f.read().split("\n")[:-1]
	r = [l[i:i+3] for i in range(0, len(l), 3)]

print(r)

s = 0
for x in r:
	for y in x[0]:
		if (y in x[1]) and (y in x[2]):
			c = ord(y)
			c -= (38 if c<=90 else 96)
			s += c
			break

print(s)
