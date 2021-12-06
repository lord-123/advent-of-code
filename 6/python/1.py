with open("input", "r") as file:
	fish = [int(x) for x in file.read().split(",")]

LENGTH = 256

starting_fish = fish

days = [0 for i in range(9)]
for x in fish:
	days[x] += 1

print(days)

for i in range(LENGTH):
	new = days[0]
	for j in range(8):
		days[j] = days[j+1]
	days[8] = new
	days[6] += new
	print(days)

print(sum(days))
