# --- Advent of code 2022: Day 03 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

rucksacks = open("input.txt").read().splitlines()
groups = list(zip(rucksacks, rucksacks[1:], rucksacks[2:]))[::3]
#print(groups)

def priority(c):
	if c <= "Z":
		return 27 + ord(c) - ord("A")
	return 1 + ord(c) - ord("a")

priority_sum = 0
for i in range(len(groups)):
	for item in groups[i][0]:
		if item in groups[i][1] and item in groups[i][2]:
			priority_sum -=- priority(item)
			break

print(f"Sum of the priorities of the badge-items: {priority_sum}")
assert priority_sum == 2805
# Answer time: 5:25
# Total day time: 13:16
