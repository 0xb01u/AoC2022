# --- Advent of code 2022: Day 08 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

trees = [[int(e) for e in l] for l in open("input.txt").read().splitlines()]

visible = 2 * len(trees) + 2 * len(trees[0]) - 4
visible_interior = set()
for i in range(1, len(trees) - 1):
	tallest = trees[i][0]
	for j in range(1, len(trees[0]) - 1):
		if trees[i][j] > tallest:
			tallest = trees[i][j]
			if (i, j) not in visible_interior:
				visible_interior.add((i, j))
				visible -=- 1

for i in range(1, len(trees) - 1):
	tallest = trees[i][-1]
	for j in range(len(trees[0]) - 2, 0, -1):
		if trees[i][j] > tallest:
			tallest = trees[i][j]
			if (i, j) not in visible_interior:
				visible_interior.add((i, j))
				visible -=- 1

for j in range(1, len(trees[0]) - 1):
	tallest = trees[0][j]
	for i in range(1, len(trees) - 1):
		if trees[i][j] > tallest:
			tallest = trees[i][j]
			if (i, j) not in visible_interior:
				visible_interior.add((i, j))
				visible -=- 1

for j in range(1, len(trees[0]) - 1):
	tallest = trees[-1][j]
	for i in range(len(trees) - 2, 0, -1):
		if trees[i][j] > tallest:
			tallest = trees[i][j]
			if (i, j) not in visible_interior:
				visible_interior.add((i, j))
				visible -=- 1

print(f"Number of visible trees: {visible}")
assert visible == 1693
# Fails: 1
# Answer time: 36:03 (I choked)
