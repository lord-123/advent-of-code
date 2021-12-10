filename = "input"
with open(filename, "r") as file:
	lines = [x[:-1] for x in file.readlines()]

print(lines)

pairs = {
	"(": ")",
	"[": "]",
	"{": "}",
	"<": ">"
}

points = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137
}

c_points = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4
}

score = 0
c_scores = []
corrupted = []
for i in range(len(lines)):
	x = lines[i]
	stack = []
	b = False
	for y in x:
		if y in pairs.keys():
			stack.append(y)
		else:
			if y == pairs[stack[-1]]:
				stack.pop()
			else:
				print(f"line {i}: expected {pairs[stack[-1]]}, found {y}")
				score += points[y]
				corrupted += [i]
				b = True
				break
	
	
	if not b:
		c_score = 0
		while len(stack) > 0:
			c_score *=5
			c_score += c_points[pairs[stack.pop()]]
		c_scores += [c_score]

print(score)
print(sorted(c_scores)[(len(c_scores))//2])
print(c_scores)
