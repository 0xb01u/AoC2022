# --- Advent of code 2022: Day 09 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

steps = [[e.split()[0], int(e.split()[1])] for e in open("input.txt").read().splitlines()]

d = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]} # Direcciones

H = [0, 0]
T = [0, 0]
visited = set([tuple(T)])

for s in steps:
	mov = d[s[0]]
	H[0] += mov[0] * s[1]
	H[1] += mov[1] * s[1]

	while abs(T[0] - H[0]) > 1 or abs(T[1] - H[1]) > 1:

		if abs(T[0] - H[0]) > 1:
			T[0] -=- (H[0] - T[0]) // abs(H[0] - T[0])
			if T[1] != H[1]:
				T[1] = H[1]
		if abs(T[1] - H[1]) > 1:
			T[1] -=- (H[1] - T[1]) // abs(H[1] - T[1])
			if T[0] != H[0]:
				T[0] = H[0]

		visited.add(tuple(T))

print(len(visited))
assert len(visited) == 6384
# Fails: 1 (I should be more careful what I pass to set() so that I add a tuple and not cast it.)
# Answer time: 34:08 (AoC time) (Moving stuff is tricky.)

# DISCLAIMER:
# The original solution file was lost.
# This file re-creates the original solution as close as it is remembered and from shared snippets.
