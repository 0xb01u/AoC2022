# --- Advent of code 2022: Day 05 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

drawing, movements = open("input.txt").read().split("\n\n")
movements = [list(map(int, e.split(" ")[1::2])) for e in movements.splitlines()]

# ir = intermediate representation
# basically equally-lengthed strings of letters where index i is container i + 1
# first string is topmost level
# spaces mean "no element" at that level for the i + 1-th crate
ir = [e[::2].replace("  ", " ") for e in drawing.replace("[", "").replace("]", "").split("\n")[:-1]]
# crates = list of lists for the crates
# the ith list is the i - 1-th crate
# inside each nested list, index 0 is topmost element, index -1 is bottommost
crates = [[] for i in range(len(ir[0]))]
# iterate over the intermediate representation
# (can be thought of as "transposing" the ir matrix so that rows are crates and not levels)
for i in range(len(ir)):
	for j in range(len(ir[i])):
		if ir[i][j] != " ":
			# insert element in respective crate
			crates[j].append(ir[i][j])
# TIP: next time you can use zip(*ir) to transpose it (you have to remove the spaces after, though).

# perform movements
for mv in movements:
	n = mv[0]	# number of items moved
	src = mv[1] - 1
	dst = mv[2] - 1
	moved = crates[src][:n] # items moved
	crates[src] = crates[src][n:] # "pop" from source
	crates[dst] = moved[::-1] + crates[dst] # "push" to destination
	# crates[dst] = moved + crates[dst] # replace previous with this for day 2

# reconstruct message
msg = ""
for c in crates:
	msg += c[0] # topmost element of each crate

print(f"Crates on top: {msg}")
assert msg == "QMBMJDFTD"
# Answer time: 21:18
