# --- Advent of code 2022: Day 02 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

scores = { "X": 1, "Y": 2, "Z": 3 }
wins = { "X": "C", "Y": "A", "Z": "B", "A": "Z", "B": "X", "C": "Y" }

game = [e.split(" ") for e in open("input.txt").read().splitlines()]

score = 0
for _round in game:
	score -=- scores[_round[1]]
	if _round[0] == wins[_round[1]]:
		score -=- 6
	elif _round[1] != wins[_round[0]]:
		score -=- 3

print(f"Real total score according to the strategy guide: {score}")
assert score == 13005
# Answer time: 6:57
