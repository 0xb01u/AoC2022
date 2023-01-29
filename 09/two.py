# --- Advent of code 2022: Day 09 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

steps = [[e.split()[0], int(e.split()[1])] for e in open("input.txt").read().splitlines()]

d = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]} # Direcciones

rope = [[0, 0] for e in range(10)]
visited = set([tuple(rope[9])])

for s in steps:
	amount = s[1]
	mov = d[s[0]]
	rope[0][0] += mov[0] * amount
	rope[0][1] += mov[1] * amount

	for _ in range(amount):
		for i in range(1, 10):
			T = rope[i]
			H = rope[i - 1]

			if abs(T[0] - H[0]) > 1:
				T[0] -=- (H[0] - T[0]) // abs(H[0] - T[0])
				if T[1] != H[1]:
					T[1] -=- (H[1] - T[1]) // abs(H[1] - T[1])
			if abs(T[1] - H[1]) > 1:
				T[1] -=- (H[1] - T[1]) // abs(H[1] - T[1])
				if T[0] != H[0]:
					T[0] -=- (H[0] - T[0]) // abs(H[0] - T[0])

			if i == 9:
				visited.add(tuple(T))

print(len(visited))
assert len(visited) == 2734
# Fails: 1 (Part one had a bug with diagonal movements. It took a long time to debug & find,
#          thus the high answer time.)
# Answer time: 29:20 (AoC time)
# Total day time: 01:03:28 (AoC time)

# DISCLAIMER:
# The original solution file was lost.
# This file re-creates the original solution as close as it is remembered and from shared snippets.
