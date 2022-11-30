with open("input", "r") as file:
	numbers = file.readlines()

gamma = ""

for i in range(len(numbers[0])):
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

for i in range(len(numbers[0])):
	zeroes = 0
	ones = 0

	for j in range(len(numbers)):
		if numbers[j][i] == "1":
			ones+=1
		else:
			zeroes+=1
#	print(ones, zeroes)
	epsilon += "1" if ones < zeroes else "0"

# oxygen
oxygenNumbers = numbers
for i in range(len(numbers[0])):
	if(len(oxygenNumbers) == 1): break
	ones = sum(int(x[i]) for x in oxygenNumbers)
	if ones >= len(oxygenNumbers)-ones:
		oxygenNumbers = [x for x in oxygenNumbers if x[i] == "1"]
	else:
		oxygenNumbers = [x for x in oxygenNumbers if x[i] == "0"]
	
co2Numbers = numbers
for i in range(len(numbers[0])):
	if(len(co2Numbers ) == 1): break
	ones = sum(int(x[i]) for x in co2Numbers)
	if ones < len(co2Numbers)-ones:
		co2Numbers = [x for x in co2Numbers if x[i] == "1"]
	else:
		co2Numbers = [x for x in co2Numbers if x[i] == "0"]


print(oxygenNumbers, int(oxygenNumbers[0],2))
print(co2Numbers, int(co2Numbers[0],2))
print(int(co2Numbers[0],2)*int(oxygenNumbers[0],2))
