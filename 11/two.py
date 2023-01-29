# --- Advent of code 2022: Day 11 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

inp = open("input.txt").read().splitlines()

monkeys = [list(map(int, e[len("  Starting items: "):].split(", "))) for e in inp[1::7]]
op = [compile(e[len("  Operation: new = "):], "", "eval") for e in inp[2::7]]
test = [int(e[len("  Test: divisible by "):]) for e in inp[3::7]]
if_true = [int(e[len("    If true: throw to monkey "):]) for e in inp[4::7]]
if_false = [int(e[len("    If false: throw to monkey "):]) for e in inp[5::7]]

from math import prod
mod = prod(test) # I initially discarded the idea of this being the correct solution due to
                 # being too simple, so I didn't even test it.
                 # After a lot of time wasted (thus the high Answer time) trying to find patterns
                 # in the monkeys or inspections, to predict the value for a given round using
                 # a formula, I tried this out of curiosity and desperation.
                 # Ockham's razor. Ockham's razor is real.

inspections = [0 for i in range(len(monkeys))]

for _ in range(10_000):
	for i in range(len(monkeys)):
		for old in monkeys[i]:
			inspections[i] -=- 1
			new = eval(op[i]) # Eval is faster than exec; both are slow if not using compile()
			new %= mod
			if new % test[i] == 0:
				monkeys[if_true[i]].append(new)
			else:
				monkeys[if_false[i]].append(new)
		monkeys[i] = []

business = sorted(inspections)
print(f"Level of monkey business after 10 000 rounds: {business[-1] * business[-2]}")
assert business[-1] * business[-2] == 35270398814
# Answer time: 34:37 (AoC time)
# Total day time: 01:00:57 (AoC time)

# DISCLAIMER:
# The original solution file was lost.
# This file re-creates the original solution as close as it is remembered and from shared snippets.
