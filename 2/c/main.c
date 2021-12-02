#include<stdio.h>
#include "cinput.h"

int
main()
{
	int horizontal = 0;
	int depth = 0;
	int aim = 0;

	int i;
	int x;
	for (i = 0; i < 1000; ++i)
	{
		x = commands[i][1] - '0';
		switch(commands[i][0])
		{
			case 'f':
				horizontal += x;
				depth += x * aim;
				break;
			case 'u':
				aim -= x;
				break;
			case 'd':
				aim += x;
		}
	}

	printf("%d\n", horizontal*depth);
}
