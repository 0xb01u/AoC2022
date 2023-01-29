# --- Advent of code 2022: Day 20 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

numbers = list(map(lambda e: 811589153 * int(e), open("input.txt").read().splitlines()))
indices = [i for i in range(len(numbers))]

for r in range(10):
	for _ in range(len(indices)):
		i = indices[_]
		n = numbers[i]
		numbers.pop(i)
		_i = i + n
		_i %= len(numbers)
		numbers.insert(_i, n)
		for __ in range(len(indices)):
			if _i > i:
				if indices[__] > i and indices[__] <= _i:
					indices[__] = (indices[__] - 1) % len(indices)
			else:
				if indices[__] < i and indices[__] >= _i:
					indices[__] = (indices[__] + 1) % len(indices)
		indices[_] = _i
	#print(numbers, indices)
	print(f"Mixing round {r + 1} of 10 done.")

offset = numbers.index(0)
print(f"Sum of the (correct) grove coordinates: {sum([numbers[i % len(numbers)] for i in range(1000 + offset, 3000 + offset + 1, 1000)])}")
# ~50s to get the answer, but I guess there is no incentive to optimize it further.
assert sum([numbers[i % len(numbers)] for i in range(1000 + offset, 3000 + offset + 1, 1000)]) == 11102539613040
# (I didn't time myself because I didn't have my usual timer nearby.)
