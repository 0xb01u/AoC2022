# --- Advent of code 2022: Day 15 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

report = open("input.txt").read().splitlines()

import re

sensors = {}

for sensor in report:
	pattern = re.compile(r'-?\d+')
	sx, sy, bx, by = map(int, pattern.findall(sensor))
	sensors[(sx, sy)] = (bx, by)
beacons = set(sensors.values())

manhattan = lambda a, b: abs(b[0] - a[0]) + abs(b[1] - a[1])
min_distances = { s: manhattan(s, b) for s, b in sensors.items() }

Y = 2000000
not_beacons = set()

for s in sensors:
	closest = manhattan(s, (s[0], Y))
	if closest <= min_distances[s]:
		farthest = [s[0] - min_distances[s] + closest, s[0] + min_distances[s] - closest]
		
		for x in range(farthest[0], farthest[1] + 1):
			if (x, Y) not in beacons:
				not_beacons.add(x)

print(len(not_beacons))
assert len(not_beacons) == 4560025
# Fails: 2
# Answer time: 48:51 (AoC time)
# Today's description felt hard to follow, and "scanners" and "beacons" gave me PTSD.
