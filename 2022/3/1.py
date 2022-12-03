with open("input", "r") as f:
	r = [[x[:len(x)//2]] + [x[len(x)//2:]] for x in f.read().split("\n")[:-1]]

print(r)

s = 0
for x in r:
	for y in x[0]:
		if y in x[1]:
			c = ord(y)
			c -= (38 if c <= 90 else 96)
			s += c
			print(y,c)
			break

print(s)
