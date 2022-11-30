with open("input", "r") as file:
	bits = bin(int(file.read(), 16))[2:]
	bits = "".join(['0' for i in range(4-(len(bits)%4) if len(bits)%4!=0 else 0)]) + bits

LITERAL = 4

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

def sum_versions(p, acc=0):
	acc += p[0]
	if p[1] != LITERAL:
		for x in p[3]:
			acc += sum_versions(x)
	return acc

print(sum_versions(p))
