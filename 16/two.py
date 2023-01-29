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
def score(cur, ele, closed, time_cur, time_ele):
	if time_cur > 0 and time_ele > 0 and len(closed) == 1:
		final = closed.copy().pop()

		cur_steps = nx.shortest_path_length(G, cur, final)
		ele_steps = nx.shortest_path_length(G, ele, final)
		if cur_steps < ele_steps:
			time_cur = 0
		else:
			time_ele = 0

	# Move both myself and the elephant:
	if time_cur > 0 and time_ele > 0:
		if (tuple(sorted([(cur, time_cur), (ele, time_ele)])), tuple(list(closed))) in scores:
			return scores[(tuple(sorted([(cur, time_cur), (ele, time_ele)])), tuple(list(closed)))]

		if len(closed) == 0:
			return [(time_cur - 1) * flow_rate[cur] + (time_ele - 1) * flow_rate[ele], [cur], [ele]]

		possible_scores = []
		path_forward_cur = []
		path_forward_ele = []
		for other in closed:
			new = closed - { other }

			shortest_path = nx.shortest_path(G, cur, other)
			shortest_path_set = set(shortest_path)

			if len(new & shortest_path_set) > 1:
				'''
				See part one's code for an explanation on why
				this condition shouldn't work but maybe it actually should.
				'''
				continue

			# Choose the elephant's target:
			for other_other in new:
				if other_other in shortest_path_set:
					continue

				new_new = new - { other_other } 

				shortest_path_ele = nx.shortest_path(G, ele, other_other)
				shortest_path_ele_set = set(shortest_path_ele)

				if len(new_new.intersection(shortest_path_ele_set)) > 1:
					continue

				res = score(other, other_other, new_new, time_cur - len(shortest_path), time_ele - len(shortest_path_ele))
				possible_scores.append(res[0])
				path_forward_cur.append(res[1])
				path_forward_ele.append(res[2])

		hi_score = max(possible_scores)
		path_cur = path_forward_cur[possible_scores.index(hi_score)]
		path_ele = path_forward_ele[possible_scores.index(hi_score)]
		scores[(tuple(sorted([(cur, time_cur), (ele, time_ele)])), tuple(list(closed)))] = [(time_cur - 1) * flow_rate[cur] + (time_ele - 1) * flow_rate[ele] + max(possible_scores), [cur] + path_cur, [ele] + path_ele]
		return scores[(tuple(sorted([(cur, time_cur), (ele, time_ele)])), tuple(list(closed)))]

	# Move only myself, the elephant has no time left:
	elif time_cur > 0:
		if (cur, time_cur, tuple(list(closed))) in scores:
			return scores[(cur, time_cur, tuple(list(closed)))]

		if len(closed) == 0:
			return [(time_cur - 1) * flow_rate[cur], [cur], []]

		possible_scores = []
		path_forward_cur = []
		for other in closed:
			new = closed - { other }

			shortest_path = nx.shortest_path(G, cur, other)
			shortest_path_set = set(shortest_path)

			if len(new & shortest_path_set) > 1:
				continue

			res = score(other, None, new, time_cur - len(shortest_path), 0)
			possible_scores.append(res[0])
			path_forward_cur.append(res[1])

		hi_score = max(possible_scores)
		scores[(cur, time_cur, tuple(list(closed)))] = [(time_cur - 1) * flow_rate[cur] + max(possible_scores), [cur] + path_forward_cur[possible_scores.index(hi_score)], []]
		return scores[(cur, time_cur, tuple(list(closed)))]

	# Move only the elephant, I do not have time left:
	elif time_ele > 0:
		if (ele, time_ele, tuple(list(closed))) in scores:
			return scores[(ele, time_ele, tuple(list(closed)))]

		if len(closed) == 0:
			return [(time_ele - 1) * flow_rate[ele], [], [ele]]

		possible_scores = []
		path_forward_ele = []
		for other in closed:
			new = closed - { other }

			shortest_path_ele = nx.shortest_path(G, ele, other)
			shortest_path_ele_set = set(shortest_path_ele)

			if len(new & shortest_path_ele_set) > 1:
				continue

			res = score(None, other, new, 0, time_ele - len(shortest_path_ele))
			possible_scores.append(res[0])
			path_forward_ele.append(res[2])

		hi_score = max(possible_scores)
		scores[(ele, time_ele, tuple(list(closed)))] = [(time_ele - 1) * flow_rate[ele] + hi_score, [], [ele] + path_forward_ele[possible_scores.index(hi_score)]]
		return scores[(ele, time_ele, tuple(list(closed)))]

	return [0, [], []]

print(*score("AA", "AA", flowing_valves, 27, 27)) # ~6.5min (384s) to get the solution on a somewhat fast PC (i7 7700K).
# 2591 ['AA', 'NU', 'YA', 'EJ', 'XK', 'DG'] ['AA', 'NV', 'PS', 'FX', 'JM', 'KZ', 'UX', 'DO']

# Fails 1 (2580, too low, at 3170 tested unpruned cases, it was worth a try.)
