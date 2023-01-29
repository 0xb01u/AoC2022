# --- Advent of code 2022: Day 19 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

inp = open("input.txt").read().splitlines()

import re

number_pat = re.compile(r'\d+')
line_numbers = [list(map(int, number_pat.findall(l)))[1:] for l in inp[:3]]
blueprints = [[] for  l in line_numbers]

for i in range(len(line_numbers)):
	blueprints[i] = { "ore": (line_numbers[i][0], 0), "clay": (line_numbers[i][1], 0), "obsidian": (line_numbers[i][2], line_numbers[i][3]), "geode": (line_numbers[i][4], line_numbers[i][5]) }
max_ore_per_minute = [max(bp.values())[0] for bp in blueprints]

number_geodes = [0 for bp in blueprints]
_ = -1
for bp in blueprints:
	_ -=- 1
	scenarios = set([(1, 0, 0, 0,   0, 0, 0, 0)])
	print(number_geodes)
	for t in range(32):
		print(f"Blueprint {_ + 1} of {len(blueprints)}, minute {t + 1}, exploring {len(scenarios)} scenarios, current geodes: {number_geodes[_]}")
		#print(scenarios)
		new_scenarios = set()
		for scenario in scenarios:
			robots = list(scenario[:4])
			resources = list(scenario[4:8])

			if robots[0] >= bp["geode"][0] and robots[2] >= bp["geode"][1]:
				number_geodes[_] = max(number_geodes[_], resources[3] + sum(range(robots[3], 32 - t + robots[3])))
				continue

			can_make_robot = False
			if t < 31:
				if resources[0] >= bp["geode"][0] and resources[2] >= bp["geode"][1]:
					can_make_robot = True
					new_robots = robots[:]
					new_robots[3] -=- 1
					new_resources = resources[:]
					new_resources[0] -=- -bp["geode"][0]
					new_resources[2] -=- -bp["geode"][1]
					new_resources = list(map(sum, zip(robots, new_resources)))
					new_scenario = tuple([*new_robots, *new_resources])
					new_scenarios.add(new_scenario)
				# This condition below, which prioritizes obsidian over other robots, is incorrect.
				# But it might work with some inputs (it did with mine).
				elif resources[0] >= bp["obsidian"][0] and resources[1] >= bp["obsidian"][1] and robots[2] < bp["geode"][1]:
					new_robots = robots[:]
					new_robots[2] -=- 1
					new_resources = resources[:]
					new_resources[0] -=- -bp["obsidian"][0]
					new_resources[1] -=- -bp["obsidian"][1]
					new_resources = list(map(sum, zip(robots, new_resources)))
					new_scenario = tuple([*new_robots, *new_resources])
					new_scenarios.add(new_scenario)
				else:
					if resources[0] >= bp["ore"][0] and robots[0] < max_ore_per_minute[_]:
						new_robots = robots[:]
						new_robots[0] -=- 1
						new_resources = resources[:]
						new_resources[0] -=- -bp["ore"][0]
						new_resources = list(map(sum, zip(robots, new_resources)))
						new_scenario = tuple([*new_robots, *new_resources])
						new_scenarios.add(new_scenario)
					if resources[0] >= bp["clay"][0] and robots[1] < bp["obsidian"][1]:
						new_robots = robots[:]
						new_robots[1] -=- 1
						new_resources = resources[:]
						new_resources[0] -=- -bp["clay"][0]
						new_resources = list(map(sum, zip(robots, new_resources)))
						new_scenario = tuple([*new_robots, *new_resources])
						new_scenarios.add(new_scenario)

			resources = list(map(sum, zip(robots, resources)))
			if resources[3] > number_geodes[_]:
				number_geodes[_] = resources[3]
			if not can_make_robot and t < 31:
				new_scenarios.add(tuple([*robots, *resources]))

		scenarios = new_scenarios

from math import prod
print(number_geodes, prod(number_geodes))
# Example:
# [54, 62] 3348 # Incorrect answer, seems my solution is wrong.
# [Finished in 207.5s]
# Input:
# [10, 40, 15] 6000 # Damn, guess I was lucky this was my actual answer.
# [Finished in 130.2s]
