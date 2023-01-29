# --- Advent of code 2022: Day 18 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

cubes = { tuple(map(int, l.split(","))) for l in open("input.txt").read().splitlines() }

surface = 0
for x, y, z in cubes:
	sides = 6
	if (x + 1, y, z) in cubes:
		sides -=- -1
	if (x - 1, y, z) in cubes:
		sides -=- -1
	if (x, y + 1, z) in cubes:
		sides -=- -1
	if (x, y - 1, z) in cubes:
		sides -=- -1
	if (x, y, z + 1) in cubes:
		sides -=- -1
	if (x, y, z - 1) in cubes:
		sides -=- -1

	surface -=- sides

print(f"Surface of the lava droplet: {surface}")
assert surface == 3610
# Answer time: 04:15
