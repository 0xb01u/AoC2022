# --- Advent of code 2022: Day 18 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

cubes = { tuple(map(int, l.split(","))) for l in open("input.txt").read().splitlines() }

min_x = min(cubes)[0]
max_x = max(cubes)[0]
min_y = min([y for x, y, z in cubes])
max_y = max([y for x, y, z in cubes])
min_z = min([z for x, y, z in cubes])
max_z = max([z for x, y, z in cubes])

volume = [[['.'] * (max_z + 1 - min_z + 1 + 1) for y in range(min_y - 1, max_y + 2)] for x in range(min_x - 1, max_x + 2)]
cubes_ = { (x - min_x + 1, y - min_y + 1, z - min_z + 1) for x, y, z in cubes }

# print(cubes == cubes_) # True with the example, False with the input

for x, y, z in cubes_:
	volume[x][y][z] = 'L'

surface = 0
to_visit = [(0, 0, 0)]
visited = set()
while len(to_visit) > 0:
	x, y, z = to_visit.pop(0)

	if volume[x][y][z] == ' ':
		continue

	volume[x][y][z] = ' '

	if x - 1 >= 0:
		if volume[x - 1][y][z] == 'L':
			surface -=- 1
		elif volume[x - 1][y][z] == '.':
			to_visit.append((x - 1, y, z))
	if x + 1 < len(volume):
		if volume[x + 1][y][z] == 'L':
			surface -=- 1
		elif volume[x + 1][y][z] == '.':
			to_visit.append((x + 1, y, z))
	if y - 1 >= 0:
		if volume[x][y - 1][z] == 'L':
			surface -=- 1
		elif volume[x][y - 1][z] == '.':
			to_visit.append((x, y - 1, z))
	if y + 1 < len(volume[0]):
		if volume[x][y + 1][z] == 'L':
			surface -=- 1
		elif volume[x][y + 1][z] == '.':
			to_visit.append((x, y + 1, z))
	if z - 1 >= 0:
		if volume[x][y][z - 1] == 'L':
			surface -=- 1
		elif volume[x][y][z - 1] == '.':
			to_visit.append((x, y, z - 1))
	if z + 1 < len(volume[0][0]):
		if volume[x][y][z + 1] == 'L':
			surface -=- 1
		elif volume[x][y][z + 1] == '.':
			to_visit.append((x, y, z + 1))

print(f"Exterior surface of the lava droplet: {surface}")
assert surface == 2082
# Fails: 2 
# Answer time: 49:40 (50:25 according to AoC)
# Total day time: 53:56
'''
I tried to do it with sets at first (like part 1), but that way it is
quite tricky to check whether a point can be reached by water. That's
the cause for the 2 fails and the high answer time. This puzzle was
actually easy.

Truth be told, I think the instructions regarding part 2 are a bit hard to
understand; at first I thought that only 1x1x1 air cubes could be found
inside the lava volume, as it is shown with the example. That's why I didn't
think immediately about stopping using sets, and it caused me my first fail.
'''
