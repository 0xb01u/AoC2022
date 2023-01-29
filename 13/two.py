# --- Advent of code 2022: Day 13 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

packets = open("input.txt").read().split("\n\n")

def compare(left, right):
	# This function returns the opposite result a standar comparison function
	# would return; i.e.: 1 if left < right, -1 if left > right
	# The reason is that when I coded it for part 1 I wasn't thinking about ordering
	# the pairs or packets, and I used the 1, 0, -1 values to code a useful result:
	#  1 means that the order is correct.
	#  0 means that there is not enough information on the order yet (or that they are equal packets)
	# -1 means that the order is incorrect.
	# It was just a coincidence that this function is usable as a reverse comparison function
	# for part 2.
	if len(left) == 0:
		return 1
	elif len(right) == 0:
		return -1

	for i in range(min(len(left), len(right))):
		if type(left[i]) == type(0) and type(right[i]) == type(0):
			if left[i] > right[i]:
				return -1
			elif left[i] < right[i]:
				return 1
		elif type(left[i]) == type([]) and type(right[i]) == type([]):
			res = compare(left[i], right[i])
			if res != 0:
				return res
			elif len(left) > len(right):
				return -1
			elif len(left) < len(right):
				return 1
		elif type(left[i]) == type([]) and type(right[i]) == type(0):
			return compare(left[i], [right[i]])
		elif type(left[i]) == type(0) and type(right[i]) == type([]):
			return compare([left[i]], right[i])

	if len(left) > len(right):
		return -1
	elif len(left) < len(right):
		return 1

	return 0

all_packets = [[[2]], [[6]]]

in_order = []
for i, pairs in enumerate(packets):
	lists = pairs.split("\n")
	left = eval(lists[0])
	right = eval(lists[1])

	all_packets.append(left)
	all_packets.append(right)

import functools

key = functools.cmp_to_key(compare)

all_packets.sort(key=key, reverse=True)

#[print(e) for e in all_packets]
print(f"Decoder key: {(all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)}")
assert (all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1) == 22852
# Answer time: 07:23 (AoC time)
# Total day time: 01:46:47 (AoC time)
# Bad day (my fault).
