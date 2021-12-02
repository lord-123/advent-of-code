with open ("input", "r") as file:
	commands = file.readlines()

horizontal = 0
depth = 0

for x in commands:
	command, num = x.split()
	num = int(num)
	if command == "forward":
		horizontal += num
	elif command == "up":
		depth -= num
	elif command == "down":
		depth += num

print(f"horizontal: {horizontal}\ndepth: {depth}\nanswer: {horizontal*depth}")
