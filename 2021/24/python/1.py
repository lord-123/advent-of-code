with open("input", "r") as file:
	commands = [x.strip("\n").split(" ") for x in file.readlines()]

variable_names = "wxyz"
variables = { x: 0 for x in variable_names }

get_input = lambda: int(input())

instructions = {
	"inp": lambda: get_input(),
	"add": lambda a, b: a + b, 
	"mul": lambda a, b: a * b,
	"div": lambda a, b: a // b,
	"mod": lambda a, b: a % b,
	"eql": lambda a, b: 1 if a == b else 0
}

def argument(x):
	if x in variable_names:
		return variables[x]
	else:
		return int(x)

def evaluate(commands):
	for x in commands:
		storage = x[1]
		
		valency = len(x) - 1

		if valency == 1:
			variables[storage] = instructions[x[0]]()
		elif valency == 2:
			variables[storage] = instructions[x[0]](*[argument(i) for i in x[1:]])

		print(x, variables)

evaluate(commands)

#inp = ""
#inp_idx = 0
#def get_input():
#	global inp
#	global inp_idx
#
#	inp_idx += 1
#
#	return int(inp[inp_idx-1])
#
#for i in range(100000000000000, 99999999999999):
#	print(i)
#	if "0" in str(i):
#		continue
#
#	inp = str(i)
#	inp_idx = 0
#	evaluate(commands)
