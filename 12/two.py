# --- Advent of code 2022: Day 12 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

import networkx as nx

heightmap = open("input.txt").read().splitlines()

def heigth(src, dst, attrib=None):
	w = {chr(i): i - ord("a") for i in range(ord("a"), ord("z") + 1)}
	w["S"] = w["a"]
	w["E"] = w["z"]

	#print(src, dst)
	diff = w[heightmap[dst[0]][dst[1]]] - w[heightmap[src[0]][src[1]]]
	return diff

src = []
dst = None
for i in range(len(heightmap)):
	for j in range(len(heightmap[i])):
		if heightmap[i][j] == "a":
			src.append((i, j))
		elif heightmap[i][j] == "E":
			dst = (i, j)

G = nx.DiGraph()
G.add_nodes_from([(i, j) for j in range(len(heightmap[i])) for i in range(len(heightmap))])
# Ty Seralpa with the tip for what edges to add.
G.add_edges_from([((i, j), (i + 1, j)) for j in range(len(heightmap[i])) for i in range(len(heightmap) - 1) if heigth((i, j), (i + 1, j)) <= 1])
G.add_edges_from([((i, j), (i - 1, j)) for j in range(len(heightmap[i])) for i in range(1, len(heightmap)) if heigth((i, j), (i - 1, j)) <= 1])
G.add_edges_from([((i, j), (i, j + 1)) for j in range(len(heightmap[i]) - 1) for i in range(len(heightmap)) if heigth((i, j), (i, j + 1)) <= 1])
G.add_edges_from([((i, j), (i, j - 1)) for j in range(1, len(heightmap[i])) for i in range(len(heightmap)) if heigth((i, j), (i, j - 1)) <= 1])

path_lens = []
for start in src:
	if nx.has_path(G, start, dst):
		path_lens.append(nx.shortest_path_length(G, start, dst))

print(f"Fewest steps required to move to the location with the best signal from any location with elevation 'a': {min(path_lens)}")
assert min(path_lens) == 439
# Answer time: 03:32 (AoC time)
# Total day time: 01:52:22 (AoC time)
