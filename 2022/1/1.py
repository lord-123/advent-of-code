with open("input.txt", "r") as file:
	txt = [list(map(int, x.split("\n"))) for x in file.read()[:-1].split("\n\n")]


print(txt)

print(max(list(map(sum, txt))))
print(sum(sorted(list(map(sum, txt)))[-3:]))
