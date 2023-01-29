# --- Advent of code 2022: Day 21 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

monkeys = { m: op for m, op in map(lambda l: l.split(": "), open("input.txt").read().splitlines()) }
monkeys["root"] = monkeys["root"][:5] + "==" + monkeys["root"][6:]
del monkeys["humn"]

unfinished = set(monkeys.keys())
unfinished.remove("root")

while len(unfinished) > 0:
	print(f"{len(unfinished)} monkeys remaining.")
	op = monkeys["root"].split(" ")

	new_op = ""
	for p in op:
		if p in unfinished:
			new_op += f"( {monkeys[p]} )"
			unfinished.remove(p)
		else:
			new_op += p

	monkeys["root"] = new_op

# Solve equation:
test = monkeys["root"].split("==")
if "humn" in test[0]:
	rhs, lhs = test
else:
	lhs, rhs = test

rhs = rhs[1:-1]

while rhs != "humn":
	rhs_ = rhs
	new_rhs	= ""

	parenthesis_level = 0

	for c in rhs_:
		c_ = c
		if c == "(":
			parenthesis_level -=-  1
		elif c == ")":
			parenthesis_level -=- -1
		elif parenthesis_level > 0 and c == "+":
			c_ = "__sum__"
		elif parenthesis_level > 0 and c == "-":
			c_ = "__sub__"
		elif parenthesis_level > 0 and c == "*":
			c_ = "__prod__"
		elif parenthesis_level > 0 and c == "/":
			c_ = "__div__"
		new_rhs += c_

	split_op = ""
	opposite_op = ""
	if "+" in new_rhs:
		split_op = "+"
		opposite_op	= "-"
	elif "-" in new_rhs:
		split_op = "-"
		opposite_op = "+"
	elif "*" in new_rhs:
		split_op = "*"
		opposite_op = "/"
	elif "/" in new_rhs:
		split_op = "/"
		opposite_op = "*"

	#print(lhs, " and ",  rhs, split_op, opposite_op)
	for i, p in enumerate(new_rhs.split(split_op)):
		if "humn" not in p:
			if i == 0:
				if split_op == "-":
					lhs = f"-({lhs})" + opposite_op + p.replace("__sum__", "+").replace("__sub__", "-").replace("__prod__", "*").replace("__div__", "/")
				elif split_op == "/":
					lhs = p.replace("__sum__", "+").replace("__sub__", "-").replace("__prod__", "*").replace("__div__", "/") + "/" + f"({lhs})"
				else:
					lhs = f"({lhs})" + opposite_op + p.replace("__sum__", "+").replace("__sub__", "-").replace("__prod__", "*").replace("__div__", "/")
			else:
				lhs = f"({lhs})" + opposite_op + p.replace("__sum__", "+").replace("__sub__", "-").replace("__prod__", "*").replace("__div__", "/")

		else:
			rhs = p.replace("__sum__", "+").replace("__sub__", "-").replace("__prod__", "*").replace("__div__", "/")
			if rhs[0] == "(" and rhs[-1] == ")":
				rhs = rhs[1:-1]

	#print(lhs, " and ", rhs)
print()

val = int(eval(lhs))
print(f"I yell the number {val}")
assert val == 3272260914328
# (I didn't time myself because my smartphone broke on 20 Dec. and that's what I was using as timer :C)
# Answer time: 56:36 (AoC time)
