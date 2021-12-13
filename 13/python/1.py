with open("input", "r") as file:
	points, folds = file.read().split("\n\n")
	points = [tuple([int(y) for y in x.split(",")]) for x in points.split("\n")]
	points = set(points)
	folds = [(x[11], int(x[13:])) for x in folds.split("\n")[:-1]]

for fold in folds:
	if fold[0] == "y":
		points = set([(x[0], fold[1] - (x[1] - fold[1])) if x[1] > fold[1] else x for x in points])
	else:
		points = set([(fold[1] - (x[0] - fold[1]), x[1]) if x[0] > fold[1] else x for x in points])

print(len(points))

width = max(x[0] for x in points) + 1
height = max(x[1] for x in points) + 1

display = [[" " for x in range(width)] for y in range(height)]

for x in points:
	display[x[1]][x[0]] = "#"

for x in display:
	print("".join(x))
