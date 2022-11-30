f = lambda a: sum(x<y for x,y in zip(a,a[1:]))

with open("input", "r") as file:
	depths = [int(x) for x in file.readlines()]

print(f(depths))
