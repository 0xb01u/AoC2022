# --- Advent of code 2022: Day 16 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

import networkx as nx, re

report = open("input.txt").read().splitlines()

valve_pat = re.compile(r'[A-Z]{2}')
flow = re.compile(r'\d+')

flow_rate = {}
paths = {}

for line in report:
	src = valve_pat.search(line)[0]
	flow_rate[src] = int(flow.search(line)[0])
	paths[src] = valve_pat.findall(line)[1:]

G = nx.DiGraph()
G.add_nodes_from(valve for valve in paths)
G.add_edges_from((src, dst) for src in paths for dst in paths[src])

flowing_valves = { valve for valve in flow_rate if flow_rate[valve] > 0 }

closer_flowing_valves_cache = { (cave, tuple(sorted(flowing_valves))): { valve for valve in flowing_valves if valve != cave and len((flowing_valves - { valve, cave }) & set(nx.shortest_path(G, cave, valve))) == 0 } for cave in flowing_valves | { "AA" } }
def closer_flowing_valves(cave, closed):
	if (cave, tuple(sorted(closed))) in closer_flowing_valves_cache:
		return closer_flowing_valves_cache[(cave, tuple(sorted(closed)))]

	# TAKE TIME INTO ACCOUNT
	closer_flowing_valves_cache[(cave, tuple(sorted(closed)))] = { valve for valve in closed if len((closed - { valve, cave }) & set(nx.shortest_path(G, cave, valve))) <= 1 }
	return closer_flowing_valves_cache[(cave, tuple(sorted(closed)))]

scores = {}
def score(cur, closed, time):
	if time <= 0:
		return [0, []]

	if (cur, time, tuple(list(closed))) in scores:
		return scores[(cur, time, tuple(list(closed)))]

	nexts = closer_flowing_valves(cur, closed)

	if len(nexts) == 0:
		return [(time - 1) * flow_rate[cur], [cur]]

	possible_scores = []
	path_forward = []
	for other in nexts:
		new = closed - { other }

		min_steps = nx.shortest_path_length(G, cur, other)

		res = score(other, new, time - min_steps - 1)
		possible_scores.append(res[0])
		path_forward.append(res[1])

	hi_score = max(possible_scores)
	scores[(cur, time, tuple(list(closed)))] = [(time - 1) * flow_rate[cur] + hi_score, [cur] + path_forward[possible_scores.index(hi_score)]]
	return scores[(cur, time, tuple(list(closed)))]

print(*score("AA", flowing_valves, 31))
# 1923 ['AA', 'NV', 'PS', 'FX', 'JM', 'KZ', 'UX', 'DO', 'PH', 'DG']
# 1651 [AA, DD, BB, JJ, HH, EE, CC]

# First defeat of this year, accepted at 1 hour 13 minutes in.
