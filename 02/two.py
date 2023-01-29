# --- Advent of code 2022: Day 02 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

scores_X = { "A": 3, "B": 1, "C": 2 }
scores_Y = { "A": 1, "B": 2, "C": 3 }
scores_Z = { "A": 2, "B": 3, "C": 1 }
scores = { "X": (0, scores_X), "Y": (3, scores_Y), "Z": (6, scores_Z) }

game = [e.split(" ") for e in open("input.txt").read().splitlines()]

score = 0
for _round in game:
	score -=- scores[_round[1]][0]
	score -=- scores[_round[1]][1][_round[0]]

print(f"Total score according to the strategy guide: {score}")
assert score == 11373
# Answer time: 4:17
# Total day time: 11:14
