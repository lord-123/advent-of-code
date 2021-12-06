with open("input", "r") as file:
	f = [int(x) for x in file.read().split(",")]
	x = [f.count(k) for k in range(9)]

for _ in range(256):
	x = x[1:]+x[:1]
	x[6]+=x[8]

print(sum(x))
