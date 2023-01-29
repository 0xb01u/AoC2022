# --- Advent of code 2022: Day 19 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

inp = open("input.txt").read().splitlines()

# Scenario = (robots of each type, resources of each type, time)
# robots = set({ "ore": 1, "clay": 0, "obsidian": 0, "geode": 0 })
# resources = set({ "ore": 0, "clay": 0, "obsidian": 0, "geode": 0 })
specific_ingredient = { "obsidian": "clay", "geode": "obsidian" }

import re

number_pat = re.compile(r'\d+')
line_numbers = [list(map(int, number_pat.findall(l)))[1:] for l in inp]
blueprints = [[] for  l in line_numbers]

for i in range(len(line_numbers)):
	blueprints[i] = { "ore": (line_numbers[i][0], 0), "clay": (line_numbers[i][1], 0), "obsidian": (line_numbers[i][2], line_numbers[i][3]), "geode": (line_numbers[i][4], line_numbers[i][5]) }
max_ore_per_minute = [max(bp.values())[0] for bp in blueprints]

number_geodes = [0 for bp in blueprints]
_ = -1
for bp in blueprints:
	_ -=- 1
	scenarios = set([(1, 0, 0, 0,   0, 0, 0, 0,   24)])
	#print(number_geodes)
	for t in range(24):
		print(f"Blueprint {_ + 1} of {len(blueprints)}, minute {t + 1}, exploring {len(scenarios)} scenarios, current geodes: {number_geodes[_]}")
		#print(scenarios)
		new_scenarios = set()
		for scenario in scenarios:
			robots = list(scenario[:4])
			resources = list(scenario[4:8])
			time = scenario[-1] - 1

			if t < 23:
				if resources[0] >= bp["ore"][0] and robots[0] < max_ore_per_minute[_]:
					new_robots = robots[:]
					new_robots[0] -=- 1
					new_resources = resources[:]
					new_resources[0] -=- -bp["ore"][0]
					new_resources = list(map(sum, zip(robots, new_resources)))
					new_scenario = tuple([*new_robots, *new_resources, time])
					new_scenarios.add(new_scenario)
				if resources[0] >= bp["clay"][0] and robots[1] < bp["obsidian"][1]:
					new_robots = robots[:]
					new_robots[1] -=- 1
					new_resources = resources[:]
					new_resources[0] -=- -bp["clay"][0]
					new_resources = list(map(sum, zip(robots, new_resources)))
					new_scenario = tuple([*new_robots, *new_resources, time])
					new_scenarios.add(new_scenario)
				if resources[0] >= bp["obsidian"][0] and resources[1] >= bp["obsidian"][1] and robots[2] < bp["geode"][1]:
					new_robots = robots[:]
					new_robots[2] -=- 1
					new_resources = resources[:]
					new_resources[0] -=- -bp["obsidian"][0]
					new_resources[1] -=- -bp["obsidian"][1]
					new_resources = list(map(sum, zip(robots, new_resources)))
					new_scenario = tuple([*new_robots, *new_resources, time])
					new_scenarios.add(new_scenario)
				if resources[0] >= bp["geode"][0] and resources[2] >= bp["geode"][1]:
					new_robots = robots[:]
					new_robots[3] -=- 1
					new_resources = resources[:]
					new_resources[0] -=- -bp["geode"][0]
					new_resources[2] -=- -bp["geode"][1]
					new_resources = list(map(sum, zip(robots, new_resources)))
					new_scenario = tuple([*new_robots, *new_resources, time])
					new_scenarios.add(new_scenario)

			resources = list(map(sum, zip(robots, resources)))
			if resources[3] > number_geodes[_]:
				number_geodes[_] = resources[3]
			if t < 23:
				new_scenarios.add(tuple([*robots, *resources, time]))

		scenarios = new_scenarios

print(number_geodes, sum(map(lambda a: a[0] * a[1], zip(number_geodes, range(1, len(number_geodes) + 1)))))
# ~71s for the example
# ~127-171s for the input
