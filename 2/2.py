with open("input", "r") as file:
	commands = file.readlines()

aim = 0
horizontal = 0
depth = 0

for x in commands:
	command, num = x.split()
	num = int(num)

	if command == "forward":
		horizontal += num
		depth += num * aim
	elif command == "down":
		aim += num
	elif command == "up":
		aim -= num

print(horizontal*depth)
