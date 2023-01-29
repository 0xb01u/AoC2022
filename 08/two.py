# --- Advent of code 2022: Day 08 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

trees = [[int(e) for e in l] for l in open("input.txt").read().splitlines()]

def sight(i, j):
	score = 1
	h = trees[i][j]

	visible = 1
	for _i in range(i - 1, 0, -1):
		if trees[_i][j] < h:
			visible	-=- 1
		else:
			break
	score *= visible

	visible = 1
	for _i in range(i + 1, len(trees) - 1):
		if trees[_i][j] < h:
			visible	-=- 1
		else:
			break
	score *= visible

	visible = 1
	for _j in range(j - 1, 0, -1):
		if trees[i][_j] < h:
			visible	-=- 1
		else:
			break
	score *= visible

	visible = 1
	for _j in range(j + 1, len(trees[0]) - 1):
		if trees[i][_j] < h:
			visible	-=- 1
		else:
			break
	score *= visible

	return score

hiscore = 0
for i in range(1, len(trees) - 1):
	for j in range(1, len(trees) - 1):
		score = sight(i, j)
		if score > hiscore:
			hiscore	= score

print(f"Highest scenic score: {hiscore}")
assert hiscore == 422059
# Fails: 1
# Answer time: 21:22  (I choked)
# Total day time: 57:25 (I definitely choked)
