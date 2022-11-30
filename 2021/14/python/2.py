with open("input", "r") as file:
	template, rules = file.read().split("\n\n")
	rules = [x.split(" -> ") for x in rules.split("\n")[:-1]]
	rules = { x[0]: x[1] for x in rules }
	pairs = { x: 0 for x in rules.keys() }

for i in range(len(template)-1):
	pairs[template[i] + template[i+1]] += 1

print(pairs)


for _ in range(40):
	new_pairs = { x: 0 for x in rules.keys() }
	for x in pairs.keys():
		if x[0] + rules[x] in pairs.keys():
			new_pairs[x[0] + rules[x]] += pairs[x]
		if rules[x] + x[1] in pairs.keys():
			new_pairs[rules[x] + x[1]] += pairs[x]
	pairs = new_pairs

print(new_pairs)

counts = { x: 0 for x in set("".join(pairs.keys())) }
for x in pairs.keys():
	counts[x[0]] += pairs[x]
	counts[x[1]] += pairs[x]
for x in counts.keys():
	counts[x] = counts[x]//2 + counts[x]%2


print(counts)
print(max(counts.values()) - min(counts.values()))
