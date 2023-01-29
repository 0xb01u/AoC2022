# --- Advent of code 2022: Day 04 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

pairs = [e.split(",") for e in open("input.txt").read().splitlines()]

overlapped = 0
for p in pairs:
	section_range_1 = list(map(int, p[0].split("-")))
	section_range_2 = list(map(int, p[1].split("-")))
	if ((section_range_1[0] <= section_range_2[0] and section_range_1[1] >= section_range_2[0])
		or (section_range_1[0] <= section_range_2[1] and section_range_1[1] >= section_range_2[1])
		or (section_range_2[0] <= section_range_1[0] and section_range_2[1] >= section_range_1[0])
		or (section_range_2[0] <= section_range_1[1] and section_range_2[1] >= section_range_1[1])):
		overlapped -=- 1

print(f"Amount of assignment pairs that overlap: {overlapped}")
assert overlapped == 956
# Answer time: 3:13
# Total day time: 10:20
