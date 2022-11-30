with open("input") as file:
	pos = [int(x) for x in file.read().split(",")]

shortest = 99999999999999999999999
for i in range(max(pos)+1):
	total = 0
	for x in pos:
		n = abs(x-i)
		total+= (n*(n+1))//2
	if total < shortest:
		shortest = total

print(shortest)
