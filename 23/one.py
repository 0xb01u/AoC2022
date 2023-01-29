# --- Advent of code 2022: Day 23 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

grove = [list(l) for l in open("input.txt").read().splitlines()]

elves = { (j, i): None for j in range(len(grove[0])) for i in range(len(grove)) if grove[i][j] == "#" }

considered_directions = ["N", "S", "W", "E"]

for i in range(10):
	new_elves = {}
	propositions = {}
	for elf in elves:
		x, y = elf

		if (x - 1, y - 1) not in elves and (x, y - 1) not in elves and (x + 1, y - 1) not in elves \
			and (x + 1, y) not in elves and (x - 1, y) not in elves \
			and (x + 1, y + 1) not in elves and (x, y + 1) not in elves and (x - 1, y + 1) not in elves:
			elves[elf] = elf
		else:
			for dir_ in considered_directions:
				elves[elf] = elf
				if dir_ == "N":
					if (x - 1, y - 1) not in elves and (x, y - 1) not in elves and (x + 1, y - 1) not in elves:
						elves[elf] = (x, y - 1)
						break
				elif dir_ == "S":
					if (x - 1, y + 1) not in elves and (x, y + 1) not in elves and (x + 1, y + 1) not in elves:
						elves[elf] = (x, y + 1)
						break
				elif dir_ == "W":
					if (x - 1, y - 1) not in elves and (x - 1, y) not in elves and (x - 1, y + 1) not in elves:
						elves[elf] = (x - 1, y)
						break
				elif dir_ == "E":
					if (x + 1, y - 1) not in elves and (x + 1, y) not in elves and (x + 1, y + 1) not in elves:
						elves[elf] = (x + 1, y)
						break

		if elves[elf] not in propositions:
			propositions[elves[elf]] = 0
		propositions[elves[elf]] -=- 1

	for elf in elves:
		if propositions[elves[elf]] == 1:
			new_elves[elves[elf]] = None
		else:
			new_elves[elf] = None

	considered_directions = considered_directions[1:] + considered_directions[:1]
	elves = new_elves

min_x = min(elves.keys())[0]
max_x = max(elves.keys())[0]
min_y = min([y for x, y in elves.keys()])
max_y = max([y for x, y in elves.keys()])

empty_ground = 0
for i in range(min_y, max_y + 1):
	#s = ""
	for j in range(min_x, max_x + 1):
		if (j, i) not in elves:
			empty_ground -=- 1
			#s += "."
		#else:
			#s += "#"
	#print(s)

print(f"Empty ground tiles after 10 rounds: {empty_ground}")
assert empty_ground == 3906
# (I didn't time myself because my smartphone broke on 20 Dec. and that's what I was using as timer :C)
