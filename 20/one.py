# --- Advent of code 2022: Day 20 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

numbers = list(map(int, open("input.txt").read().splitlines()))
numbers = list(zip(numbers, [0] * len(numbers)))

moved = 0
i = 0
while moved < len(numbers):
	n, f = numbers[i]
	if f == 1:
		i -=- 1
		continue
	moved -=- 1
	numbers.pop(i)
	_i = (i + n) % len(numbers) # WARNING: len(numbers) is 1 less than usual. Last line was a pop().
	numbers.insert(_i, (n, 1))
	#print(numbers, i)

numbers = [n for n, f in numbers]

offset = numbers.index(0)
print(f"Sum of the grove coordinates: {sum([numbers[i % len(numbers)] for i in range(1000 + offset, 3000 + offset + 1, 1000)])}")
assert sum([numbers[i % len(numbers)] for i in range(1000 + offset, 3000 + offset + 1, 1000)]) == 11073
# Fails: 1 (Do not assume numbers only appear once)
# (I didn't time myself because I didn't have my usual timer nearby.)
