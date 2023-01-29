# --- Advent of code 2022: Day 06 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

datastream = open("input.txt").read()

for i in range(4, len(datastream) + 1):
	marker = datastream[i-4:i]
	if len(set(marker)) == 4:
		print(f"Characters processed until start-of-packet marker: {i}")
		assert i == 1175
		exit()
# Answer time: 06:57 (AoC page reports 07:01)
