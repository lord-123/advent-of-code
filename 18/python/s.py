
def convert(num):
	l = []
	number = 0
	reading_num = False
	for x in num:
		if x.isdigit():
			reading_num = True
			number *= 10
			number += int(x)
		else:
			if reading_num:
				reading_num = False
				l += [number]
				number = 0
			if x in "[]":
				l += [x]
	
	return l

def explode(num):
	l = num[:]
	depth = 0
	first_seen = False
	found = False
	for i, x in enumerate(l):
		if x == "[":
			depth += 1
			first_seen=False
		elif x == "]":
			depth -= 1
			first_seen=False
		elif isinstance(x, int) and depth >= 5:
			if not first_seen:
				first = x
				first_pos = i
				first_seen = True
			else:
				second = x
				found = True
				break
	
	if found:
		for i in range(first_pos + 2, len(l)):
			if isinstance(l[i], int):
				l[i] += second
				break
		for i in range(first_pos - 1, -1, -1):
			if isinstance(l[i], int):
				l[i] += first
				break
		del l[first_pos]
		l[first_pos] = 0
		del l[first_pos+1]
		del l[first_pos-1]

	return l

def spl(l):
	for i, x in enumerate(l):
		if isinstance(x, int):
			if x >= 10:
				l = l[:i] + ["["] + [x//2] + [x//2+x%2] + ["]"] + l[i+1:]
				break
	return l

def depth(l):
	dd = 0
	d = 0
	for x in l:
		if x == "[":
			dd += 1
			if dd > d:
				d = dd
		elif x == "]":
			dd -= 1
	return d

def reduce(l):
	while True:
		print(strl(l))
		if depth(l) >= 5:
			print("explode")
			l = explode(l)
		elif max(x for x in l if isinstance(x, int)) >= 10:
			print("split")
			l = spl(l)
		else:
			break
	return l

def add(a, b):
	new = ["["] + a + b + ["]"]

	return reduce(new)

def strl(l):
	s = ""
	for i, x in enumerate(l[:-1]):
		s += str(x)
		if (isinstance(x,int) and l[i+1] != "]") or (x=="]" and l[i+1] != "]"):
			s+=","
	s+="]"
	return s

def magnitude(l):
	total = 0
	if isinstance(l[0], int):
		total += l[0]*3
	else:
		total += magnitude(l[0])*3

	if isinstance(l[1], int):
		total += l[1]*2
	else:
		total += magnitude(l[1])*2
	
	return total

with open("input", "r") as file:
	numbers = [convert(x.strip("\n")) for x in file.readlines()]

#k = [[[[[9,8],1],2],3],4]
#k = [7,[6,[5,[4,[3,2]]]]]
#k = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
#print_l(convert(str(k)))
#print_l(reduce(convert(str(k))))

acc = numbers[0]
for x in numbers:
	acc = add(acc, x)

print(strl(acc))
print(magnitude(eval(strl(acc))))

print(magnitude([[1,2],[[3,4],5]]))
