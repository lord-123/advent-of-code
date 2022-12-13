import functools

with open("input", "r") as file:
	p =[list(map(eval, x.split("\n"))) for x in file.read()[:-1].split("\n\n")]

def compare(left, right):
	if isinstance(left, int) and isinstance(right, int):
		if left > right: return False
		elif left < right: return True
		else: return None
	elif isinstance(left, list) and isinstance(right, list):
		for a, b in zip(left, right):
			r = compare(a, b)
			if r is not None: return r
		if len(right) < len(left): return False
		if len(right) > len(left): return True
		return None
	else:
		if isinstance(left, int):
			return compare([left], right)
		else:
			return compare(left, [right])

#p1
idx = []
for i, x in enumerate(p, 1):
	(a, b) = x
	if compare(a, b): idx += [i]

print(sum(idx))

#p2
p = sum(p, [])
p += [[[2]]]
p += [[[6]]]

p = sorted(p, key=functools.cmp_to_key(lambda a, b: -1 if compare(a,b) else 1))
print((p.index([[2]])+1)*(p.index([[6]])+1))
