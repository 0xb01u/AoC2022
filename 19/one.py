# --- Advent of code 2022: Day 19 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3

MINUTES = 24

raw_blueprints = open("input.txt").read().splitlines()

import re

number_pat = re.compile(r'\d+')
blueprint_numbers = [list(map(int, number_pat.findall(l)))[1:] for l in raw_blueprints]
blueprints = [[] for  l in blueprint_numbers]

for i in range(len(blueprint_numbers)):
	blueprints[i] = { \
						"ore": (blueprint_numbers[i][0], 0), \
						"clay": (blueprint_numbers[i][1], 0), \
						"obsidian": (blueprint_numbers[i][2], blueprint_numbers[i][3]), \
						"geode": (blueprint_numbers[i][4], blueprint_numbers[i][5]) \
					}
max_ore_needed_per_minute = [max(bp.values())[0] for bp in blueprints]

largest_number_geodes = [0 for bp in blueprints]

for _, bp in enumerate(blueprints):
	scenarios = set([(1, 0, 0, 0,   0, 0, 0, 0)])
	print(str(largest_number_geodes[:_])[1:-1])

	for t in range(MINUTES):
		print(f"Blueprint {_ + 1} of {len(blueprints)}, minute {t + 1}, exploring {len(scenarios)} scenarios, current geodes: {largest_number_geodes[_]}")
		#print(scenarios)

		new_scenarios = set()
		for scenario in scenarios:
			robots = list(scenario[:4])
			resources = list(scenario[4:8])

			# Prune branches that cannot surpass current highest,
			# even if they magically reached their best scenario immediately:
			max_possible_geodes = resources[GEODE] + sum(range(robots[GEODE], MINUTES - t + robots[GEODE]))
			if max_possible_geodes < largest_number_geodes[_]:
				continue

			# If we are getting enough materials to build a geode robot per minute (best scenario),
			# return max possible geode count for this branch and prune it:
			if robots[ORE] >= bp["geode"][0] and robots[OBSIDIAN] >= bp["geode"][1]:
				largest_number_geodes[_] = max(largest_number_geodes[_], max_possible_geodes)
				continue

			# If the branch is unable to make more obsidian in time to build more geode robots, compute and
			# return the amount of geodes that will have mined in the remaining time and prune the branch:
			if resources[OBSIDIAN] + robots[OBSIDIAN] * (MINUTES - t) + (MINUTES - t) * (MINUTES - t) // 2 < bp["geode"][1]:
				largest_number_geodes[_] = max(largest_number_geodes[_], resources[GEODE] + (MINUTES - t) * robots[GEODE])
				continue

			if t < MINUTES - 1: # Don't add scenerios if in the last iteration
				can_make_geode_robot = False
				can_make_robots = [False] * 3

				# If a geode robot can be built, do it instead of anything else:
				if resources[ORE] >= bp["geode"][0] and resources[OBSIDIAN] >= bp["geode"][1]:
					can_make_geode_robot = True

					new_resources = resources[:]
					new_resources[ORE] -=- -bp["geode"][0]
					new_resources[OBSIDIAN] -=- -bp["geode"][1]
					new_resources = list(map(sum, zip(robots, new_resources))) # Add resources mined this minute

					new_robots = robots[:]
					new_robots[GEODE] -=- 1

					new_scenario = tuple([*new_robots, *new_resources])
					new_scenarios.add(new_scenario)
				else:
					# Build obsidian robot, only if we can and we are not getting enough obisidan to build one geode robot per minute:
					if resources[ORE] >= bp["obsidian"][0] and resources[CLAY] >= bp["obsidian"][1] and robots[OBSIDIAN] < bp["geode"][1] \
						and not (resources[ORE] - robots[ORE] >= bp["obsidian"][0] and resources[CLAY] - robots[CLAY] >= bp["obsidian"][1]):
					# Do not build robot if it could have been built in the previous minute
						can_make_robots[OBSIDIAN] = True

						new_resources = resources[:]
						new_resources[ORE] -=- -bp["obsidian"][0]
						new_resources[CLAY] -=- -bp["obsidian"][1]
						new_resources = list(map(sum, zip(robots, new_resources))) # Add resources mined this minute

						new_robots = robots[:]
						new_robots[OBSIDIAN] -=- 1

						new_scenario = tuple([*new_robots, *new_resources])
						new_scenarios.add(new_scenario)
					# Build ore robot, only if we can and we are not getting enough ore to build one of any robot per minute:
					if resources[ORE] >= bp["ore"][0] and robots[ORE] < max_ore_needed_per_minute[_] \
						and not (resources[ORE] - robots[ORE] >= bp["ore"][0]):
					# Do not build robot if it could have been built in the previous minute
						can_make_robots[ORE] = True

						new_resources = resources[:]
						new_resources[ORE] -=- -bp["ore"][0]
						new_resources = list(map(sum, zip(robots, new_resources))) # Add resources mined this minute

						new_robots = robots[:]
						new_robots[ORE] -=- 1

						new_scenario = tuple([*new_robots, *new_resources])
						new_scenarios.add(new_scenario)
					# Build clay robot, only if we can and we are not getting enough clay to build one obsidian robot per minute,
					# and if we are not getting enough obsidian to build one geode robot per minute (clay -> obsidian -> geode):
					if resources[ORE] >= bp["clay"][0] and robots[CLAY] < bp["obsidian"][1] and robots[OBSIDIAN] < bp["geode"][1] \
						and not (resources[ORE] - robots[ORE] >= bp["clay"][0]):
					# Do not build robot if it could have been built in the previous minute
						can_make_robots[CLAY] = True

						new_resources = resources[:]
						new_resources[ORE] -=- -bp["clay"][0]
						new_resources = list(map(sum, zip(robots, new_resources))) # Add resources mined this minute

						new_robots = robots[:]
						new_robots[CLAY] -=- 1

						new_scenario = tuple([*new_robots, *new_resources])
						new_scenarios.add(new_scenario)

			# Add resources mined this minute
			resources = list(map(sum, zip(robots, resources)))
			if resources[GEODE] > largest_number_geodes[_]:
				largest_number_geodes[_] = resources[GEODE]

			# Add scenario in which no robot has been built only if:
			#  - Not in the last iteration
			#  - A geode robot could not have been built
			#  [ - At least one of the other robots could not have been built] <- pruning these produces an incorrect answer in part one (not part two).
			#                                                                  Reason being, in the next minute a geode robot may be built, which might
			#                                                                  or might not result in a high-geode branch.
			#                                                                  (Checking if that is the case is slower than not pruning.)
			if not can_make_geode_robot and t < MINUTES - 1:
				new_scenarios.add(tuple([*robots, *resources]))

		scenarios = new_scenarios

print(f"Quality level for each blueprint: {str(largest_number_geodes)[1:-1]}\nSum of all the quality levels: {sum(map(lambda a: a[0] * a[1], zip(largest_number_geodes, range(1, len(largest_number_geodes) + 1))))}")
assert sum(map(lambda a: a[0] * a[1], zip(largest_number_geodes, range(1, len(largest_number_geodes) + 1)))) == 600

'''
Optimizations:
https://libreddit.kavin.rocks/r/adventofcode/comments/zpihwi/2022_day_19_solutions/j0w4yek/?context=3
https://libreddit.kavin.rocks/r/adventofcode/comments/zpihwi/2022_day_19_solutions/j0vvtdt/?context=3
https://libreddit.kavin.rocks/r/adventofcode/comments/zpihwi/2022_day_19_solutions/j0vupbf/?context=3
'''
