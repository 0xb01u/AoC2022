# --- Advent of code 2022: Day 22 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

turn_right = { ">": "v", "v": "<", "<": "^", "^": ">" }
turn_left = { ">": "^", "v": ">", "<": "v", "^": "<" }
move = { ">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1) }
facing_numbers = { ">": 0, "v": 1, "<": 2, "^": 3 }

# This solution works with my input's shape (which seems to be every input's shape).

example = False
example_reshaped = False

# Faces:
if example:
	board, path = open("example.txt").read().split("\n\n")

	LENGTH = 4

	A = { "x": ( 8, 12), "y": ( 0,  4) }
	B = { "x": ( 0,  4), "y": ( 4,  8) }
	C = { "x": ( 4,  8), "y": ( 4,  8) }
	D = { "x": ( 8, 12), "y": ( 4,  8) }
	E = { "x": ( 8, 12), "y": ( 8, 12) }
	F = { "x": (12, 16), "y": ( 8, 12) }
	face_ranges = { "A": A, "B": B, "C": C, "D": D, "E": E, "F": F }

	# Neighbors and relation to each neighbor
	neighbor = {
		"A": { "^": "B", "<": "C", ">": "F", "v": "D" },
		"B": { "^": "A", "<": "F", ">": "C", "v": "E" },
		"C": { "^": "A", "<": "B", ">": "D", "v": "E" },
		"D": { "^": "A", "<": "C", ">": "F", "v": "E" },
		"E": { "^": "D", "<": "C", ">": "F", "v": "B" },
		"F": { "^": "D", "<": "E", ">": "A", "v": "B" }
	}
	neighbor_border = { 
		"A": { "B": "-y", "C": "-y", "F": "+x", "D": "-y" },
		"B": { "A": "-y", "F": "+y", "C": "-x", "E": "+y" },
		"C": { "A": "-x", "B": "+x", "D": "-x", "E": "-x" },
		"D": { "A": "+y", "C": "+x", "F": "-y", "E": "-y" },
		"E": { "D": "+y", "C": "+y", "F": "-x", "B": "+y" },
		"F": { "D": "+x", "E": "+x", "A": "+x", "B": "-x" }
	}
elif example_reshaped:
	board, path = open("example_reshaped.txt").read().split("\n\n")

	LENGTH = 4

	A = { "x": ( 8, 12), "y": ( 0,  4) }
	B = { "x": ( 4,  8), "y": ( 0,  4) }
	C = { "x": ( 4,  8), "y": ( 4,  8) }
	D = { "x": ( 4,  8), "y": ( 8, 12) }
	E = { "x": ( 0,  4), "y": ( 8, 12) }
	F = { "x": ( 0,  4), "y": (12, 16) }
	face_ranges = { "A": A, "B": B, "C": C, "D": D, "E": E, "F": F }

	# Neighbors and relation to each neighbor
	neighbor = {
		"A": { "^": "F", "<": "B", ">": "D", "v": "C" },
		"B": { "^": "F", "<": "E", ">": "A", "v": "C" },
		"C": { "^": "B", "<": "E", ">": "A", "v": "D" },
		"D": { "^": "C", "<": "E", ">": "A", "v": "F" },
		"E": { "^": "C", "<": "B", ">": "D", "v": "F" },
		"F": { "^": "E", "<": "B", ">": "D", "v": "A" }
	}
	neighbor_border = { 
		"A": { "F": "+y", "B": "+x", "D": "+x", "C": "+x" },
		"B": { "F": "-x", "E": "-x", "A": "-x", "C": "-y" },
		"C": { "B": "+y", "E": "-y", "A": "+y", "D": "-y" },
		"D": { "C": "+y", "E": "+x", "A": "+x", "F": "+x" },
		"E": { "C": "-x", "B": "-x", "D": "-x", "F": "-y" },
		"F": { "E": "+y", "B": "-y", "D": "+y", "A": "-y" }
	}
else:
	board, path = open("input.txt").read().split("\n\n")

	LENGTH = 50

	A = { "x": (100, 150), "y": (  0,  50) }
	B = { "x": ( 50, 100), "y": (  0,  50) }
	C = { "x": ( 50, 100), "y": ( 50, 100) }
	D = { "x": ( 50, 100), "y": (100, 150) }
	E = { "x": (  0,  50), "y": (100, 150) }
	F = { "x": (  0,  50), "y": (150, 200) }
	face_ranges = { "A": A, "B": B, "C": C, "D": D, "E": E, "F": F }

	# Neighbors and relation to each neighbor
	neighbor = {
		"A": { "^": "F", "<": "B", ">": "D", "v": "C" },
		"B": { "^": "F", "<": "E", ">": "A", "v": "C" },
		"C": { "^": "B", "<": "E", ">": "A", "v": "D" },
		"D": { "^": "C", "<": "E", ">": "A", "v": "F" },
		"E": { "^": "C", "<": "B", ">": "D", "v": "F" },
		"F": { "^": "E", "<": "B", ">": "D", "v": "A" }
	}
	neighbor_border = { 
		"A": { "F": "+y", "B": "+x", "D": "+x", "C": "+x" },
		"B": { "F": "-x", "E": "-x", "A": "-x", "C": "-y" },
		"C": { "B": "+y", "E": "-y", "A": "+y", "D": "-y" },
		"D": { "C": "+y", "E": "+x", "A": "+x", "F": "+x" },
		"E": { "C": "-x", "B": "-x", "D": "-x", "F": "-y" },
		"F": { "E": "+y", "B": "-y", "D": "+y", "A": "-y" }
	}
dir_to_border = { "^": "-y", "<": "-x", ">": "+x", "v": "+y" }
border_to_dir = { "+x": "<", "-x": ">", "+y": "^", "-y": "v" }

def in_face(pos: tuple[int, int], face: dict[str, tuple[int, int]]) -> bool:
	x, y = pos
	return x >= face["x"][0] and x < face["x"][1] and y >= face["y"][0] and y < face["y"][1]

def direction_out(pos: tuple[int, int], face: dict[str, tuple[int, int]]) -> chr:
	x, y = pos
	if x < face["x"][0]:
		return "<"
	elif x >= face["x"][1]:
		return ">"
	elif y < face["y"][0]:
		return "^"
	elif y >= face["y"][1]:
		return "v"

opposite_sign = { "+": "-", "-": "+" }
def transform_coords(pos: tuple[int, int], dir_: chr, src: chr, dst: chr):
	border1 = dir_to_border[dir_] # Border you left from, relative to src
	border2 = neighbor_border[src][dst] # Border you enter from, relative to dst

	x, y = pos
	sign_src, coord_src = list(border1)
	sign_dst, coord_dst = list(border2)

	if coord_src == coord_dst:
		if sign_src == opposite_sign[sign_dst]:
			new_pos = (x % LENGTH + face_ranges[dst]["x"][0], y % LENGTH + face_ranges[dst]["y"][0])
		else:
			new_pos = (face_ranges[dst]["x"][1] - x % LENGTH - 1, face_ranges[dst]["y"][1] - y % LENGTH - 1)
	else:
		if sign_src == opposite_sign[sign_dst]:
			new_pos = (y % LENGTH + face_ranges[dst]["x"][0], x % LENGTH + face_ranges[dst]["y"][0])
		elif coord_src == "x":
			new_pos = (y % LENGTH + face_ranges[dst]["x"][0], face_ranges[dst]["y"][1] - x % LENGTH - 1)
		else: # coord_src == "y"
			new_pos = (face_ranges[dst]["x"][1] - y % LENGTH - 1, x % LENGTH + face_ranges[dst]["y"][0])

	return new_pos, border_to_dir[border2]

''' # Original function logic:
	if border1 == "+x":
		# (51, 0)
		if border2 == "+x":
			# (49, 0)
			return (face_ranges[dst]["x"][1] - x % LENGTH - 1, face_ranges[dst]["y"][1] - y % LENGTH - 1), "<"
		elif border2 == "-x":
			# (1, 0)
			return (x % LENGTH + face_ranges[dst]["x"][0], y % LENGTH + face_ranges[dst]["y"][0]), dir_
		elif border2 == "+y":
			# (0, 49)
			return (y % LENGTH + face_ranges[dst]["x"][0], face_ranges[dst]["y"][1] - x % LENGTH - 1), "^"
		elif border2 == "-y":
			# (0, 1)
			return (y % LENGTH + face_ranges[dst]["x"][0], x % LENGTH + face_ranges[dst]["y"][0]), "v"
	elif border1 == "-x":
		# (-1, 0)
		if border2 == "+x":
			# (49, 0)
			return (x % LENGTH + face_ranges[dst]["x"][0], y % LENGTH + face_ranges[dst]["y"][0]), dir_
		elif border2 == "-x":
			# (1, 0)
			return (face_ranges[dst]["x"][1] - x % LENGTH - 1, face_ranges[dst]["y"][1] - y % LENGTH - 1), ">"
		elif border2 == "+y":
			# (0, 49)
			return (y % LENGTH + face_ranges[dst]["x"][0], x % LENGTH + face_ranges[dst]["y"][0]), "^"
		elif border2 == "-y":
			# (0, 1)
			return (y % LENGTH + face_ranges[dst]["x"][0], face_ranges[dst]["y"][1] - x % LENGTH - 1), "v"
	elif border1 == "+y":
		# (0, 51)
		if border2 == "+x":
			# (49, 0)
			return (face_ranges[dst]["x"][1] - y % LENGTH - 1, x % LENGTH + face_ranges[dst]["y"][0]), "<"
		elif border2 == "-x":
			# (1, 0)
			return (y % LENGTH + face_ranges[dst]["x"][0], x % LENGTH + face_ranges[dst]["y"][0]), ">"
		elif border2 == "+y":
			# (0, 49)
			return (face_ranges[dst]["x"][1] - x % LENGTH - 1, face_ranges[dst]["y"][1] - y % LENGTH - 1), "^"
		elif border2 == "-y":
			# (0, 1)
			return (x % LENGTH + face_ranges[dst]["x"][0], y % LENGTH + face_ranges[dst]["y"][0]), dir_
	elif border1 == "-y":
		# (0, -1)
		if border2 == "+x":
			# (49, 0)
			return (y % LENGTH + face_ranges[dst]["x"][0], x % LENGTH + face_ranges[dst]["y"][0]), "^"
		elif border2 == "-x":
			# (1, 0)
			return (face_ranges[dst]["x"][1] - y % LENGTH - 1, x % LENGTH + face_ranges[dst]["y"][0]), ">"
		elif border2 == "+y":
			# (0, 49)
			return (x % LENGTH + face_ranges[dst]["x"][0], y % LENGTH + face_ranges[dst]["y"][0]), dir_
		elif border2 == "-y":
			# (0, 1)
			return (face_ranges[dst]["x"][1] - x % LENGTH - 1, face_ranges[dst]["y"][1] - y % LENGTH - 1), "v"

	print("FIRE!")
	exit()
'''

walkable = set()

pos = None

board = board.splitlines()
for i, line in enumerate(board):
	for j, c in enumerate(line):
		#print(c, end="")
		if c == '.':
			if pos == None:
				pos = (j, i)
			walkable.add((j, i))
	#print()

import re

movement_pat = re.compile(r"\d\d?[LR]?")
movements = movement_pat.findall(path)
movements = list(map(lambda e: (int(e[:-1]), e[-1]), movements[:-1])) + [(int(movements[-1]), "")]

facing = ">"
current_face = "A" if example else "B"
for steps, turn in movements:
	for i in range(steps):
		x, y = pos
		sx, sy = move[facing]
		next_face = current_face
		next_facing = facing

		nx = x + sx
		ny = y + sy

		if not in_face((nx, ny), face_ranges[current_face]):
			next_face = neighbor[current_face][facing]
			#print(f"From {current_face} to {next_face}: {nx, ny, facing}")
			npos, next_facing = transform_coords((nx, ny), facing, current_face, next_face)
			nx, ny = npos
			#print(f"New coords: {nx, ny, next_facing}")

		if (nx, ny) not in walkable:
			break
		pos = (nx, ny)

		current_face = next_face
		facing = next_facing

		#print(pos, facing)

	if turn == "R":
		facing = turn_right[facing]
	elif turn == "L":
		facing = turn_left[facing]

print("Final coords and facing: ", pos, facing)
col, row = pos
print (f"Real final password: {1000 * (row + 1) + 4 * (col + 1) + facing_numbers[facing]}")
assert 1000 * (row + 1) + 4 * (col + 1) + facing_numbers[facing] == 162155
# Fails: 2 (One transform_coords() case was wrong, and another thing)
# (I didn't time myself because my smartphone broke on 20 Dec. and that's what I was using as timer :C)
