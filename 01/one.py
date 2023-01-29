# --- Advent of code 2022: Day 01 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

elves = [sum(list(map(int, x.splitlines()))) for x in open("input.txt").read().split("\n\n")]
print(f"Calories carried by the highest-calories carrying elf: {max(elves)}")
assert max(elves) == 66306
# Answer time: 3:23
