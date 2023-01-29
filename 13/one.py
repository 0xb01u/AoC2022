# --- Advent of code 2022: Day 13 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

packets = open("input.txt").read().split("\n\n")

def compare(left, right):
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

in_order = []
for i, pairs in enumerate(packets):
	lists = pairs.split("\n")
	left = eval(lists[0])
	right = eval(lists[1])

	order = compare(left, right)
	#print(pairs, order)
	if order == 1: # 1 == order is correct; -1 == order is not correct
		in_order.append(i + 1)

print(f"Sum of the indices of the in-order pairs: {sum(in_order)}")
assert sum(in_order) == 5555
# Fails: 1
# Answer time: 01:39:24 (AoC time)
# I wasted >1h trying to reuse my solution for 2021 day 18 (i.e. the intermediate representation used).
# First I thought it would work out-of-the-box, then I realized some caveats that made it not work
# for today's puzzle, and tried uselessly to make it work.
# "Prematura optimization is the root of all evil." - Donald Knuth
