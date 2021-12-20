with open("input", "r") as file:
	t = [x.strip("\n") for x in file.readlines()]
	algorithm = t[0]
	image = t[2:]

def enhance(image, algorithm, inf="."):
	pad = "".join([inf for i in range(len(image) + 4)])
	image = [pad] + [pad] + [inf*2 + x + inf*2 for x in image] + [pad] + [pad]
	
#	for x in image:
#		print(x)
	
	out = []
	for i in range(1, len(image)-1):
		out += [""]
		for j in range(1, len(image[i])-1):
			idx = image[i-1][j-1:j+2] + image[i][j-1:j+2] + image[i+1][j-1:j+2]
			x = 0
			for y in idx:
				x*=2
				if y == "#":
					x+=1
			out[-1] += algorithm[x]
			#print("i", i, "j", j, "idx:", idx)
	
	for x in out:
		print(x)
	
	return out

a = enhance(image, algorithm)
b = enhance(a, algorithm, "#")

print(sum(x.count("#") for x in b))
