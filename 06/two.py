# --- Advent of code 2022: Day 06 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

datastream = open("input.txt").read()

for i in range(14, len(datastream) + 1):
	marker = datastream[i-14:i]
	if len(set(marker)) == 14:
		print(f"Characters processed until start-of-message marker: {i}")
		assert i == 3217
		exit()
# Answer time: 00:40 (AoC page reports 00:41)
# Total day time: 07:37 (AoC page reports 07:41)
