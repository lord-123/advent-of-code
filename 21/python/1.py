# test
pos = {
	1: 4,
	2: 8
}
# real
pos = {
	1: 6,
	2: 2
}

die = 1
die_count = 0
turn = 1

scores = {
	1: 0,
	2: 0
}
while max(scores.values()) < 1000:
	for i in range(3):
		pos[turn] += die
		if pos[turn] > 10:
			new_pos = pos[turn] % 10
			if new_pos == 0:
				new_pos = 10
			pos[turn] = new_pos
		die += 1
		die_count+=1
		if die == 101:
			die = 1
	scores[turn] += pos[turn]
	turn = 2 if turn == 1 else 1

	print(pos, scores)

print(scores)
print(min(scores.values()) * die_count)
