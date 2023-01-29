# --- Advent of code 2022: Day 15 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

import re

sensors = { (sx, sy): (bx, by) for sx, sy, bx, by in [map(int, re.compile(r'-?\d+').findall(l)) for l in open("input.txt").read().splitlines()] }

min_coord = 0
max_coord = 4000000

manhattan = lambda a, b: abs(b[0] - a[0]) + abs(b[1] - a[1])
min_distances = { s: manhattan(s, b) for s, b in sensors.items() }

corners = []
for s in sensors:
	sx, sy = s
	s_corners = []
	s_corners.extend([(sx - min_distances[s] - 1, sy), (sx + min_distances[s] + 1, sy)])
	s_corners.extend([(sx, sy - min_distances[s] - 1), (sx, sy + min_distances[s] + 1)])
	corners.append(s_corners)

sensors_ = sorted(sensors.keys(), key=lambda s: min_distances[s], reverse=True)

for s in corners:
	print(f"Testing perimeter of sensor #{corners.index(s) + 1}")
	perimeter = set()

	d = abs(s[0][0] - s[2][0])
	for i in range(d + 1):
		# The distress beacon must (should) be surrounded by 4 different rhomboidal ranges.
		# Each of the surrounding rhomboids will be "touching" the beacon with a different border
		# (i.e. the upper left, upper right, lower right or lower left border).
		# Thus, for all four border types, there is one rhomboid that touches the beacon with that
		# particular border. That means that we can check just one of the borders for all the sensors
		# and we will eventually find the beacon.
		# Exception: if the beacon is at the border of the valid coordinates (min_x, min_y, max_y, max_y).
		# I don't know if such an input exists.
		#
		# In this specific implementation (targetting my input), I choose to compute the border
		# I know a posteriori that will find the beacon in the least amount of checked sensors.
		# Any other border can be chosen, but the time difference may be considerable.

		# perimeter.add((s[0][0] + i, s[0][1] - i))
		perimeter.add((s[0][0] + i, s[0][1] + i))
		# perimeter.add((s[1][0] - i, s[1][1] + i))
		# perimeter.add((s[1][0] - i, s[1][1] - i))

	for p in perimeter:
		px, py = p
		if px < min_coord or px > max_coord or py < min_coord or py > max_coord:
			continue

		distress = True
		for s_ in sensors_: # Check sensors with higher detection range first. More likely to rule out this point.
			if manhattan(s_, p) <= min_distances[s_]:
				distress = False
				break

		if distress:
			print(px * 4000000 + py)
			assert px * 4000000 + py == 12480406634249
			# p == (3120101, 2634249)
			exit()

assert False
# Answer time: 01:34:55 (AoC time)
# Total day time: 02:23:12 (AoC time)
# Slow but steady. Lost a lot of time trying to find a way to check if a point was inside a
# rhomboid given the point and the coords of the rhomboid, because I didn't realized I could
# use the range of the beacon instead.

# Some friend sent me this regarding a faster solution (I think he found it on reddit):
#
# > I do not completely agree with the statement "you can't brute force it".
# > You can't brute force 16 trillion individual points but checking 4 million lines with a clever computation
# > about computing the coverage of each line ends in 3 sec on my newish MB Pro.
# > 
# > The main trick to a manageable brute force solution is to make sure you calculate coverage within a line
# > purely on the from and to value of each individual range of coverage and not expand the coverage into a list,
# > array, set whatever your language is best at. In other words can you quickly merge / form the union of two ranges
# > that you have defined only by their 2 limits?
# > 
# > If you do that you end up with a handful of additions and ifs and a loop only over the limited sets of sensors per line with no significant memory overhead.
