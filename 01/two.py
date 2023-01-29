# --- Advent of code 2022: Day 01 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

elves = [sum(list(map(int, x.splitlines()))) for x in open("input.txt").read().split("\n\n")]
print(f"Calories carried by the highest-calories carrying elf: {sum(sorted(elves, reverse=True)[:3])}")
assert sum(sorted(elves, reverse=True)[:3]) == 195292
# Answer time: 1:52 (I forgot to reverse the sort and had to wait 1 more min to give the right answer.)
# Total day time: 5:15
