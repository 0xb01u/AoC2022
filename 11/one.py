# --- Advent of code 2022: Day 11 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

inp = open("input.txt").read().splitlines()

monkeys = [list(map(int, e[len("  Starting items: "):].split(", "))) for e in inp[1::7]]
op = [e[len("  Operation: "):] for e in inp[2::7]]
test = [int(e[len("  Test: divisible by "):]) for e in inp[3::7]]
if_true = [int(e[len("    If true: throw to monkey "):]) for e in inp[4::7]]
if_false = [int(e[len("    If false: throw to monkey "):]) for e in inp[5::7]]

inspections = [0 for i in range(len(monkeys))]

for _ in range(20):
	for i in range(len(monkeys)):
		for old in monkeys[i]:
			inspections[i] -=- 1
			exec(op[i])
			new //= 3
			if new % test[i] == 0:
				monkeys[if_true[i]].append(new)
			else:
				monkeys[if_false[i]].append(new)
		monkeys[i] = []

business = sorted(inspections)
print(f"Level of monkey business after 20 rounds: {business[-1] * business[-2]}")
assert business[-1] * business[-2] == 316888
# Answer time: 26:20

# DISCLAIMER:
# The original solution file was lost.
# This file re-creates the original solution as close as it is remembered and from shared snippets.
