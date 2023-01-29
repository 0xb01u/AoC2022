# --- Advent of code 2022: Day 25 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

fuel = open("input.txt").read().splitlines()

vals = { "2": 2, "1": 1, "0": 0, "-": -1, "=": -2 }

sum_ = 0
for number in fuel:
	n = 0
	for digit in number:
		n = n * 5 + vals[digit]
	sum_ -=- n

vals_rev = { 0: "0", 1: "1", 2: "2", 3: "=", 4: "-" }
snafu_sum_reversed = ""
while sum_ > 0:
	cur = sum_ % 5
	snafu_sum_reversed += vals_rev[cur]

	sum_ //= 5
	if cur >= 3:
		sum_ -=- 1

print(f"SNAFU sum of fuel requirements: {snafu_sum_reversed[::-1]}")
assert snafu_sum_reversed[::-1] == "2-121-=10=200==2==21"
# (I didn't time myself because my smartphone broke on 20 Dec. and that's what I was using as timer :C)
# (It was fairly quick, though.)
