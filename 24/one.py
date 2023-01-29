# --- Advent of code 2022: Day 24 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

valley = open("input.txt").read().splitlines()

dirs = { ">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1), "": (0, 0) }

blizzards = {}
for i in range(1, len(valley) - 1):
	for j in range(1, len(valley[0]) - 1):
		if valley[i][j] != '.':
			blizzards[(j - 1, i - 1)] = [valley[i][j]]

max_x = j
max_y = i

# For debugging the blizzards
def print_valley():
	for i in range(max_y):
		s = ""
		for j in range(max_x):
			if (j, i) in blizzards:
				if len(blizzards[(j, i)]) > 1:
					s += str(len(blizzards[(j, i)]))
				else:
					s += blizzards[(j, i)][0]
			else:
				s += "."
		print(s)
	print()

pos = set([(0, -1)])
dst = (max_x - 1, max_y)

finished = False
steps = 0
while not finished:
	steps -=- 1
	#print(f"Step #{steps}, positions to check: {len(pos)}")

	# Move blizzards:
	new_blizzards = {}
	for p, blizzards_ in blizzards.items():
		for blizzard_dir in blizzards_:
			x, y = p
			dx, dy = dirs[blizzard_dir]

			nx = (x + dx) % max_x
			ny = (y + dy) % max_y

			if (nx, ny) not in new_blizzards:
				new_blizzards[(nx, ny)] = []
			new_blizzards[(nx, ny)].append(blizzard_dir)

	blizzards = new_blizzards
	new_pos = set()

	# Explore movement possibilities:
	for p in pos:
		x, y = p
		for d in dirs.values():
			dx, dy = d
			nx = x + dx
			ny = y + dy


			if (nx, ny) == dst:
				finished = True
				break
			elif nx != nx % max_x or ny != ny % max_y:
				continue
			elif (nx, ny) not in blizzards:
				new_pos.add((nx, ny))


		if finished:
			break

	pos = new_pos
	pos.add((0, -1)) # You can always wait at the entrance

print(f"Fewest minutes required to reach the goal: {steps}")
assert steps == 326
# (I didn't time myself because my smartphone broke on 20 Dec. and that's what I was using as timer :C)
