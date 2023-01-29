# --- Advent of code 2022: Day 17 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

gas = open("input.txt").read().strip()

rocks = [
		[(0, 0), (1, 0), (2, 0), (3, 0)],
		[(0, 1), (1, 1), (1, 0), (1, 2), (2, 1)],
		[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
		[(0, 0), (0, 1), (0, 2), (0, 3)],
		[(0, 0), (0, 1), (1, 0), (1, 1)]
	]

def _print(fallen, highest, rock):
	for _i in range(-4, highest):
		s = ""
		for _rocks_fallen in range(7):
			if (_rocks_fallen, highest - _i) in fallen:
				s += "#"
			elif rock != None and (_rocks_fallen, highest - _i) in rock:
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

states = []
heights = []
repetition_beginning = 0
repetition_end = 0
while True:
	i = (i + 1) % len(gas)

	# Appearance
	if rock == None:
		heights.append(highest)

		state = (i, rocks_fallen % len(rocks), (0, highest) in fallen, (1, highest) in fallen, (2, highest) in fallen, (3, highest) in fallen, (4, highest) in fallen, (5, highest) in fallen, (6, highest) in fallen)
		if states.count(state) > 0:
			# We are assuming there are no sub-repetitions inside or before the actual main repetition (which is the case, at least for my input).
			# If there were, we would have to check all states from the first repeated state on are repeated,
			# until finding the first repeated state again (i.e. no "gaps" of unrepeated elements).
			repetition_beginning = states.index(state)
			repetition_end = len(states) - 1
			# print(f"Repetition on fallen rock {rocks_fallen} -> {states.index(state)}: {state}")
			break
		states.append(state)

		rock = [(x + 2, y + highest + 4) for x, y in rocks[rocks_fallen % len(rocks)]]
		rocks_fallen -=- 1

		# print(fallen, highest, rock)

	# Current
	if gas[i] == ">":
		rock_ = [(x + 1, y) for x, y in rock]
	elif gas[i] == "<":
		rock_ = [(x - 1, y) for x, y in rock]
	else:
		print(f"{gas[i]=} stupid newline of doom")

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

TO_FALL = 1_000_000_000_000

period = repetition_end - repetition_beginning + 1
height_offset = heights[repetition_beginning - 1]
height_increase = heights[repetition_end] - height_offset
print(f"Tower loop starts with the fallen rock #{repetition_beginning}, has a period of {period} rocks, \
the height of the tower beforehand is {height_offset} rocks, and each period adds a height of {height_increase} units to the tower.")
repetitions = (TO_FALL - repetition_beginning + 1) // period
reminder = (TO_FALL - repetition_beginning + 1) % period
print(f"Height of the tower after 1000000000000 have fallen: {repetitions * height_increase + heights[reminder + repetition_beginning - 1]}")
assert repetitions * height_increase + heights[reminder + repetition_beginning - 1] == 1_526_744_186_042

# Fails: 4
'''
I didn't note the time because it was taking too long, I didn't know where the problem was,
eventually got fed up and decided to stop counting the time and take a break. When I came back, I
wasn't in the mood for timing myself anymore.
(Delta is 03:46:34 according to AoC, but I took some breaks between completing part one and part two.)

And it was all because the input file ended in a newline and I didn't take that into consideration...

EDIT: For some reason part one works even with the newline in the file, which is interpreted as an additional "<", WTH??
That is so (un)lucky.
'''