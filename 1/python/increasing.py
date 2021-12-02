count = 0

with open(input("in file: "), "r") as file:
	number = 999999999
	for line in file:
		if int(line) > number:
			count += 1
		number = int(line)

print(count)
