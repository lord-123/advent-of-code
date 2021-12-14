with open("input", "r") as file:
	template, rules = file.read().split("\n\n")
	rules = [x.split(" -> ") for x in rules.split("\n")[:-1]]
	rules = { x[0]: x[1] for x in rules }

polymer = template

for c in range(40):
	print(c)
	indexes = []
	for i in range(len(polymer)-1):
		pair = polymer[i]+polymer[i+1] 
		if pair in rules.keys():
			indexes += [(i, rules[pair])]
	for i, x in enumerate(indexes):
		print(len(indexes) - i)
		polymer = polymer[:x[0]+i+1] + x[1] + polymer[x[0]+i+1:]

most = max(set(polymer), key=polymer.count)
least = min(set(polymer), key=polymer.count)

print(polymer.count(most)-polymer.count(least))
