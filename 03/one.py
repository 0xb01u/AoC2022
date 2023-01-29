# --- Advent of code 2022: Day 03 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

rucksacks = [[e[:len(e) // 2], e[len(e) // 2:]] for e in open("input.txt").read().splitlines()]

def priority(c):
	if c <= "Z":
		return 27 + ord(c) - ord("A")
	return 1 + ord(c) - ord("a")

priority_sum = 0
for i in range(len(rucksacks)):
	for item in rucksacks[i][0]:
		if item in rucksacks[i][1]:
			priority_sum -=- priority(item)
			break

print(f"Sum of the priorities of the re-appearing items: {priority_sum}")
assert priority_sum == 7674
# Answer time: 7:51
