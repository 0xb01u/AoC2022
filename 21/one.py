# --- Advent of code 2022: Day 21 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

monkeys = { m: op for m, op in map(lambda l: l.split(": "), open("input.txt").read().splitlines()) }
unfinished = set(monkeys.keys())

while len(unfinished) > 0:
	print(f"{len(unfinished)} monkeys remaining.")
	for m in unfinished.copy():
		op = monkeys[m].split(" ")

		if op[0].isnumeric():
			monkeys[m] = int(op[0])
			unfinished.remove(m)
			continue

		if not type(monkeys[op[0]]) == type(0) or not type(monkeys[op[2]]) == type(0):
			continue

		if op[1] == '+':
			monkeys[m] = monkeys[op[0]] + monkeys[op[2]]
		elif op[1] == '-':
			monkeys[m] = monkeys[op[0]] - monkeys[op[2]]
		elif op[1] == '*':
			monkeys[m] = monkeys[op[0]] * monkeys[op[2]]
		elif op[1] == '/':
			monkeys[m] = monkeys[op[0]] // monkeys[op[2]]

		unfinished.remove(m)
print()

print(f"root will yell the number {monkeys['root']}")
assert monkeys["root"] == 10037517593724
# (I didn't time myself because my smartphone broke on 20 Dec. and that's what I was using as timer :C)
