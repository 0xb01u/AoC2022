# --- Advent of code 2022: Day 16 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

import networkx as nx, re

report = open("input.txt").read().splitlines()

valve = re.compile(r'[A-Z]{2}')
flow = re.compile(r'\d+')

flow_rate = {}
paths = {}

for line in report:
	src = valve.search(line)[0]
	flow_rate[src] = int(flow.search(line)[0])
	paths[src] = valve.findall(line)[1:]

G = nx.DiGraph()
G.add_nodes_from(valve for valve in paths)
G.add_edges_from((src, dst) for src in paths for dst in paths[src])

flowing_valves = { valve for valve in flow_rate if flow_rate[valve] > 0 }

scores = {}
def score(cur, closed, time):
	if time <= 0:
		return [0, []]

	if (cur, time, tuple(list(closed))) in scores:
		return scores[(cur, time, tuple(list(closed)))]

	if len(closed) == 0:
		return [(time - 1) * flow_rate[cur], [cur]]

	possible_scores = []
	path_forward = []
	for other in closed:
		new = closed - { other }

		shortest_path = nx.shortest_path(G, cur, other)
		shortest_path_set = set(shortest_path)

		if len(shortest_path_set & new) > 1:
			'''
			That this condition to decrease the search space works is a complete
			and incredible coincidence.

			The idea behind it was "do not explore the possibility of going to
			one of the closed caves if there is another in the way, since you are
			going to want to open the one in the way first to get more pressure
			released (which is a possibility explored in other iteration of this loop)".

			However and first off, using > 1 instead of > 0 is a typo. So this condition
			only prunes the possibilities where there are 2 closed caves in the path,
			which was not originally intended.

			Moreover, the remining time should be taken into account before deciding
			not to go directly to another cave just because there is another valid cave
			in the path: if the preassure the former releases in 1 minute is higher than
			the pressure released by the latter in the time it takes to go from the latter
			to the former (i.e. if the minute it takes to open the in-between cave
			is not worth it because you release more pressure with the current target),
			then the possibility should not be pruned.

			That being said, this solution seems to work when using this condition
			(with 1 and not 0 in the right hand side). Using 0 doesn't work with the
			example, but does with the input (lucky coincidence).
			The only explanation I can think of is that, when there are at least 2
			closed caves in the path, the chance of any of them (or both) not being worth
			opening first is low enough.
			'''
			continue

		res = score(other, new, time - len(shortest_path))
		possible_scores.append(res[0])
		path_forward.append(res[1])

	hi_score = max(possible_scores)
	scores[(cur, time, tuple(list(closed)))] = [(time - 1) * flow_rate[cur] + hi_score, [cur] + path_forward[possible_scores.index(hi_score)]]
	return scores[(cur, time, tuple(list(closed)))]

print(*score("AA", flowing_valves, 31))
# 1923 ['AA', 'NV', 'PS', 'FX', 'JM', 'KZ', 'UX', 'DO', 'PH', 'DG'] # Other paths seem to be also valid.

# First defeat of this year, accepted at 1 hour 13 minutes in.

'''
Seems like the correct solution is using Depth-First Search. That should give the answer
almost instantly.
Maybe that's a little tricky to integrate with networkx?

# Seralpa code:
def dfs(node: Valve, time: int, pressure: int, open_valves: frozenset[str]):  #function for dfs
    time -= 1

    if seen.get((node.name, time), -1) >= pressure:
        return seen[(node.name, time)]

    seen[(node.name, time)] = pressure

    if time == 0:
        return pressure

    net_pressure = sum(valves[valve].flow for valve in open_valves)

    scores = []
    if node.name not in open_valves and node.flow > 0:
        scores.append(dfs(node, time, pressure + net_pressure + node.flow, open_valves | {node.name}))
    for neighbour in node.tunnels:
        scores.append(dfs(neighbour, time, pressure + net_pressure, open_valves))
    return max(scores)
'''
