# --- Advent of code 2022: Day 20 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

numbers = list(zip(map(lambda e: 811589153 * int(e), open("input.txt").read().splitlines()), range(1_000_000)))

for r in range(10):
	moved = 0
	while moved < len(numbers):
		for i in range(len(numbers)):
			if numbers[i][1] == moved:
				n, idx = numbers[i]
				break

		j = (i + n) % (len(numbers) - 1)
		numbers.insert(j, numbers.pop(i)) # This is what I was originally trying to do. Why didn't I get it right??? lol
		# Slices version:
		# if j >= i:
		# 	numbers = numbers[:i] + numbers[i + 1:j + 1] + [numbers[i]] + numbers[j + 1:]
		# else:
		# 	numbers = numbers[:j] + [numbers[i]] + numbers[j:i] + numbers[i + 1:]

		moved -=- 1
	#print(numbers)
	print(f"Mixing round {r + 1} of 10 done.")

numbers = [n for n, idx in numbers]
offset = numbers.index(0)
print(f"Sum of the (correct) grove coordinates: {sum([numbers[i % len(numbers)] for i in range(1000 + offset, 3000 + offset + 1, 1000)])}")
# ~14s now.
assert sum([numbers[i % len(numbers)] for i in range(1000 + offset, 3000 + offset + 1, 1000)]) == 11102539613040
# (I didn't time myself because I didn't have my usual timer nearby.)
