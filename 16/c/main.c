#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum length_types
{
	BIT_LENGTH,
	PACKET_LENGTH
};

enum types
{
	SUM,
	PRODUCT,
	MINIMUM,
	MAXIMUM,
	LITERAL,
	GREATER_THAN,
	LESS_THAN,
	EQUAL_TO,
	TYPES_LENGTH
};

typedef struct Packet
{
	int version;
	enum types type;
	int length;

	union
	{
		long data;
		struct PacketList
		{
			int length;
			struct Packet *sub_packets;
		} PacketList;
	};
} Packet;

long
sum(long *p, long len)
{
	long acc = 0;
	int i;
	for (i = 0; i < len; i++)
		acc += p[i];

	return acc;
}

long
product(long *p, long len)
{
	long acc = p[0];
	int i;
	for (i = 1; i < len; i++)
		acc *= p[i];

	return acc;
}

long
minimum(long *p, long len)
{
	long x = p[0];
	int i;
	for (i = 1; i < len; ++i)
		if (p[i] < x)
			x = p[i];

	return x;
}

long
maximum(long *p, long len)
{
	long x = p[0];
	int i;
	for (i = 1; i < len; ++i)
		if (p[i] > x)
			x = p[i];

	return x;
}

long
greater_than(long *p, long len)
{
	return p[0] > p[1];
}

long
less_than(long *p, long len)
{
	return p[0] < p[1];
}

long
equal_to(long *p, long len)
{
	return p[0] == p[1];
}

long (*operators[])(long *, long) = 
{
	sum, product, minimum, maximum, 0, greater_than, less_than, equal_to
};

void
hex_to_bin(char x, char *bin)
{
	switch(x)
	{
		case '0':
			strcpy(bin, "0000");
			break;
		case '1':
			strcpy(bin, "0001");
			break;
		case '2':
			strcpy(bin, "0010");
			break;
		case '3':
			strcpy(bin, "0011");
			break;
		case '4':
			strcpy(bin, "0100");
			break;
		case '5':
			strcpy(bin, "0101");
			break;
		case '6':
			strcpy(bin, "0110");
			break;
		case '7':
			strcpy(bin, "0111");
			break;
		case '8':
			strcpy(bin, "1000");
			break;
		case '9':
			strcpy(bin, "1001");
			break;
		case 'A':
			strcpy(bin, "1010");
			break;
		case 'B':
			strcpy(bin, "1011");
			break;
		case 'C':
			strcpy(bin, "1100");
			break;
		case 'D':
			strcpy(bin, "1101");
			break;
		case 'E':
			strcpy(bin, "1110");
			break;
		case 'F':
			strcpy(bin, "1111");
			break;
	}
}

long
bin_to_long(char *bits, size_t len)
{
	long x = 0;
	int i;
	for (i = 0; i < len; ++i)
	{
		x = x << 1;
		if (bits[i] == '1')
			++x;
	}

	return x;
}

Packet
get_packet(char *bits)
{
	int i;
	char *start = bits;

	Packet p;
	p.version = bin_to_long(bits, 3);
	bits += 3;

	p.type = bin_to_long(bits, 3);
	bits += 3;

	if (p.type == LITERAL)
	{
		char *lit = (char *)malloc(0);
		size_t len = 4;
		while(1)
		{
			lit = (char *)realloc(lit, len * sizeof(char));
			for (i = 0; i < 4; ++i)
			{
				lit[len-4+i] = bits[i+1];
			}
			if (*bits == '0')
				break;
			else
			{
				len += 4;
				bits += 5;
			}
		}
		bits+=5;
		p.data = bin_to_long(lit, len);
		free(lit);
	}
	else
	{
		enum length_types l = *(bits++) - '0';
		int length;

		length = bin_to_long(bits, l == BIT_LENGTH ? 15 : 11);
		bits += l == BIT_LENGTH ? 15 : 11;

		p.PacketList.length = 0;
		p.PacketList.sub_packets = (Packet *)malloc(0);
		char *final = bits + length;
		for (i = 0; l == BIT_LENGTH ? bits != final : i < length; ++i)
		{
				++p.PacketList.length;
				p.PacketList.sub_packets = (Packet *)realloc(p.PacketList.sub_packets, p.PacketList.length * sizeof(Packet));
				
				p.PacketList.sub_packets[p.PacketList.length - 1] = get_packet(bits);
				bits += p.PacketList.sub_packets[p.PacketList.length - 1].length;
		}
	}

	p.length = bits - start;
	return p;
}

long
evaluate_packet(Packet p)
{
	if (p.type == LITERAL)
		return p.data;
	else
	{
		long count = p.PacketList.length;
		long *values = (long *)malloc(count * sizeof(long));
		int i;
		for (i = 0; i < count; ++i)
			values[i] = evaluate_packet(p.PacketList.sub_packets[i]);
		
		long ret = operators[p.type](values, count);
		free(values);
		return ret;
	}
}

int
main()
{
	char input[1024];
	scanf("%s", input);

	char *bits = (char *)malloc((strlen(input) * 4 + 1) * sizeof(char));
	int i = 0;
	while(input[i])
	{
		hex_to_bin(input[i], bits + i * 4);
		++i;
	}
	bits[i*4] = '\0';

	printf("%s\n", bits);

	Packet p = get_packet(bits);

	long result = evaluate_packet(p);

	printf("%ld\n", result);
}
