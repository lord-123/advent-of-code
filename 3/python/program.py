with open("input", "r") as file:
	numbers = file.readlines()

gamma = ""

for i in range(12):
	zeroes = 0
	ones = 0

	for j in range(len(numbers)):
		if numbers[j][i] == "1":
			ones+=1
		else:
			zeroes+=1
#	print(ones, zeroes)
	gamma += "1" if ones > zeroes else "0"

epsilon = ""

for i in range(12):
	zeroes = 0
	ones = 0

	for j in range(len(numbers)):
		if numbers[j][i] == "1":
			ones+=1
		else:
			zeroes+=1
#	print(ones, zeroes)
	epsilon += "1" if ones < zeroes else "0"

print(gamma, int(gamma,2))
print(epsilon, int(epsilon,2))

print(int(epsilon,2)*int(gamma,2))
