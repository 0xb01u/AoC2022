# --- Advent of code 2022: Day 17 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

gas = open("input.txt").read().strip() # The .strip() can be removed and my input stills outputs the right answer.

rocks = [
		[(0, 0), (1, 0), (2, 0), (3, 0)],
		[(0, 1), (1, 1), (1, 0), (1, 2), (2, 1)],
		[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
		[(0, 0), (0, 1), (0, 2), (0, 3)],
		[(0, 0), (0, 1), (1, 0), (1, 1)]
	]

def _print(fallen, highest, rock):
	for i in range(-4, highest):
		s = ""
		for j in range(7):
			if (j, highest - i) in fallen:
				s += "#"
			elif rock != None and (j, highest - i) in rock:
				s += "@"
			else:
				s += "."
		print(s)
	print()

fallen = set([(x, 0) for x in range(7)])
highest = 0
rock = None
i = -1
rocks_fallen = 0
while rocks_fallen < 2023:
	i = (i + 1) % len(gas)

	# Appearance
	if rock == None:
		rock = [(x + 2, y + highest + 4) for x, y in rocks[rocks_fallen % len(rocks)]]
		rocks_fallen -=- 1

		# print(fallen, highest, rock)

	# Current
	if gas[i] == ">":
		rock_ = [(x + 1, y) for x, y in rock]
	elif gas[i] == "<":
		rock_ = [(x - 1, y) for x, y in rock]

	cannot_move = False
	for x, y in rock_:
		if (x, y) in fallen or x < 0 or x >= 7:
			cannot_move = True
			break

	if not cannot_move:
		rock = rock_

	# print(fallen, highest, rock)

	# Gravity
	rock_ = [(x, y - 1) for x, y in rock]

	rest = False
	max_y = highest
	for x, y in rock_:
		max_y = max(y + 1, max_y)
		if (x, y) in fallen:
			rest = True

	if rest:
		fallen.update(rock)
		highest = max_y
		rock = None
	else:
		rock = rock_

	# print(fallen, highest, rock)

print(f"Height of the tower after 2022 have fallen: {highest}")
assert highest == 3111
# Answer time: 48:43
