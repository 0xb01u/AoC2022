# --- Advent of code 2022: Day 14 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

scan = [[list(map(int, e.split(","))) for e in l.split(" -> ")] for l in open("input.txt").read().splitlines()]

O = (500, 0)
rock = set()

for struct in scan:
	for i in range(len(struct) - 1):
		a = struct[i]
		b = struct[i + 1]
		dx = b[0] - a[0]
		dy = b[1] - a[1]

		if dx != 0:
			for x in range(abs(dx) + 1):
				rock.add((a[0] + x * dx // abs(dx), a[1]))
		if dy != 0:
			for y in range(abs(dy) + 1):
				rock.add((a[0], a[1] + y * dy // abs(dy)))

actual_rocks = len(rock)

max_y = max(e[1] for e in rock) + 2

while True:
	x = O[0]
	next_pos = None
	for y in range(O[1], max_y + 1):
		if (x, y) in rock or y == max_y:
			if (x - 1, y) in rock or y == max_y:
				if (x + 1, y) in rock or y == max_y:
					next_pos = (x, y - 1)
					break
				else:
					x -=- 1
			else:
				x -=- -1

	if next_pos == O:
		break

	rock.add(next_pos)

print(len(rock) - actual_rocks + 1)
assert len(rock) - actual_rocks + 1 == 25248
# Answer time: 01:30 (AoC time)
# Total day time: 38:09 (AoC time)
