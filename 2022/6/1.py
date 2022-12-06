with open("input", "r") as f:
	s = f.read()

w = [s[i-4:i] for i in range(4, len(s))]

for (i, x) in enumerate(w):
	if len(set(x)) == len(x):
		print(x, i+4)
		break

w = [s[i-14:i] for i in range(14, len(s))]

for (i, x) in enumerate(w):
	if len(set(x)) == len(x):
		print(x, i+14)
		break
