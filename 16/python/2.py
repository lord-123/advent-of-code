with open("input", "r") as file:
	text = file.read()
	bits = bin(int(text, 16))[2:]
	bits = "".join(['0' for i in range(4-(len(bits)%4) if len(bits)%4!=0 else 0)]) + bits
	if text[0] == "0":
		bits = "0000" + bits

LITERAL = 4

from math import prod
operators = {
	0: sum,
	1: prod,
	2: min,
	3: max,
	5: lambda x: 1 if x[0] > x[1] else 0,
	6: lambda x: 1 if x[0] < x[1] else 0,
	7: lambda x: 1 if x[0] == x[1] else 0
}

print(bits)

i = 0

def get_packet(bits, i=0):
	start = i
	version = int(bits[i:i+3], 2)
	type_id = int(bits[i+3:i+6], 2) 
	print(i, version, type_id)
	if type_id == LITERAL:
		i += 6
		parts = ""
		while int(bits[i]) == 1:
			parts += bits[i+1:i+5]
			i += 5
		parts += bits[i+1:i+5]
		i += 5
		p = (version, type_id, i-start, int(parts, 2))
		print(p)
		return p
	else:
		length_type = int(bits[i+6])
		# bit count
		if length_type == 0:
			length = int(bits[i+7:i+22], 2)
			i += 22
			final = i + length
			sub_packets = []
			while i != final:
				sub_packets += [get_packet(bits, i)]
				if len(sub_packets) > 0:
					i += sub_packets[-1][2]
			p = (version, type_id, i-start, sub_packets)
			print(p)
			return p
		# packet count
		else:
			length = int(bits[i+7:i+18], 2)
			sub_packets = []
			i += 18
			for j in range(length):
				sub_packets += [get_packet(bits, i)]
				if len(sub_packets) > 0:
					i += sub_packets[-1][2]
			return (version, type_id, i-start, sub_packets)

p = get_packet(bits)
print(p)

def evaluate_packet(p):
	print("EVALUATION")
	print(p)
	if p[1] == LITERAL:
		return p[3]
	else:
		return operators[p[1]]([evaluate_packet(x) for x in p[3]])

print(evaluate_packet(p))
