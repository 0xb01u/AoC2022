# --- Advent of code 2022: Day 05 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

drawing, movements = open("input.txt").read().split("\n\n")
movements = [list(map(int, e.split(" ")[1::2])) for e in movements.splitlines()]

ir = [e[::2].replace("  ", " ") for e in drawing.replace("[", "").replace("]", "").split("\n")[:-1]]
crates = [[] for i in range(len(ir[0]))]
for i in range(len(ir)):
	for j in range(len(ir[i])):
		if ir[i][j] != " ":
			crates[j].append(ir[i][j])

for mv in movements:
	#print(mv, crates)
	n = mv[0]
	src = mv[1]  - 1
	dst = mv[2]  - 1
	moved = crates[src][:n]
	crates[src] = crates[src][n:]
	crates[dst] = moved + crates[dst]

msg = ""
for c in crates:
	msg += c[0]

print(f"Crates on top (CrateMover 9001): {msg}")
assert msg == "NBTVTJNFJ"
# Answer time: 00:43
# Total day time: 21:18
