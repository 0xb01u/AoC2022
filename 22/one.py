# --- Advent of code 2022: Day 22 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

board, path = open("input.txt").read().split("\n\n")

turn_right = { ">": "v", "v": "<", "<": "^", "^": ">" }
turn_left = { ">": "^", "v": ">", "<": "v", "^": "<" }
move = { ">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1) }
facing_numbers = { ">": 0, "v": 1, "<": 2, "^": 3 }

min_x_coords = []
max_x_coords = []
min_y_coords = []
max_y_coords = []

walkable = set()
walls = set()

pos = None

board = board.splitlines()
for i, line in enumerate(board):
	min_x_coords.append(0)
	max_x_coords.append(0)
	for j, c in enumerate(line):
		#print(c, end="")
		if c == ' ':
			min_x_coords[i] = j + 1
		elif c == '.':
			if pos == None:
				pos = (j, i)
			walkable.add((j, i))
		elif c == '#':
			walls.add((j, i))
	#print()
	max_x_coords[i] = j + 1

for j in range(max(max_x_coords)):
	min_y_coords.append(0)
	max_y_coords.append(0)
	board_begun = False
	for i, line in enumerate(board):
		if j >= len(board[i]):
			if not board_begun:
				min_y_coords[j] = i + 1
			else:
				max_y_coords[j] = i
				break
			continue
		c = board[i][j]
		#print(c, end="")
		if c == ' ':
			if board_begun:
				max_y_coords[j] = i
				break
			else:
				min_y_coords[j] = i + 1
		elif c == '.' or c == '#':
			board_begun = True
	if max_y_coords[j] == 0:
		max_y_coords[j] = i + 1
	#print()

import re

movement_pat = re.compile(r"\d\d?[LR]?")
movements = movement_pat.findall(path)
movements = list(map(lambda e: (int(e[:-1]), e[-1]), movements[:-1])) + [(int(movements[-1]), "")]

facing = ">"
for steps, turn in movements:
	for i in range(steps):
		x, y = pos
		sx, sy = move[facing]

		nx = (x + sx - min_x_coords[y]) % (max_x_coords[y] - min_x_coords[y]) + min_x_coords[y]
		ny = (y + sy - min_y_coords[x]) % (max_y_coords[x] - min_y_coords[x]) + min_y_coords[x]
		if (nx, ny) not in walkable:
			break
		pos = (nx, ny)

	if turn == "R":
		facing = turn_right[facing]
	elif turn == "L":
		facing = turn_left[facing]

print("Final coords and facing: ", pos, facing)
col, row = pos
print (f"Final password: {1000 * (row + 1) + 4 * (col + 1) + facing_numbers[facing]}")
assert 1000 * (row + 1) + 4 * (col + 1) + facing_numbers[facing] == 43466
# Fails: 2
# (I didn't time myself because my smartphone broke on 20 Dec. and that's what I was using as timer :C)
