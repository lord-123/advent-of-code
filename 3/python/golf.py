with open("input", "r") as file:
	lines = [x[:-1] for x in file.readlines()]

print((lambda x,y:x*y)(*[sum([((lambda a,b:a<b,lambda a,b:a>b)[k](sum(int(i)for i in x),len(x)//2))*2**(len(lines[0])-j-1)for j,x in enumerate(zip(*lines))])for k in(0,1)]))
