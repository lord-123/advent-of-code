with open("input", "r") as file:
	nums = [[y.strip("\n") for y in x.split(" | ")[0].split(" ") + x.split(" | ")[1].split(" ")] for x in file.readlines()]

s = [
	set("abcefg"),
	set("cf"),
	set("acdeg"),
	set("acdfg"),
	set("bcdf"),
	set("abdfg"),
	set("abdefg"),
	set("acf"),
	set("abcdefg"),
	set("abcdfg")
]

distinct = {2: 1,4: 4,3: 7,7: 8}

total = 0
for x in nums:
	s = {i: None for i in range(10)}
	for y in x:
		if len(y) in distinct:
			s[distinct[len(y)]] = set(y)
	
	a = s[7] - s[1]
	bd = s[4] - s[1]
	eg = (s[8] - s[4]) - a
	print(f"a: {a}, bd: {bd}, eg: {eg}")

	#print(s)

	for y in x:
		if len(y) == 6:
			if len(s[1] & set(y))==2:
				if len(bd & set(y)) == 2:
					s[9] = set(y)
				else:
					s[0] = set(y)
			else:
				s[6] = set(y)
		elif len(y) == 5:
			if len(bd & set(y))==2:
				s[5] = set(y)
			else:
				if len(s[1] & set(y))==2:
					s[3] = set(y)
				else:
					s[2] = set(y)

	print (s)

	k = 0
	for i in x[-4:]:
		#print("decoding", i)
		i = set(i)
		k*=10
		k += list(s.keys())[list(s.values()).index(i)]

	total += k
print(total)
