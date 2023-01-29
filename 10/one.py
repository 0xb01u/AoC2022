# --- Advent of code 2022: Day 10 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

instructions = open("input.txt").read().splitlines()

msg = "#"
X = [0, 1] # Values of register X over time (0 added to correctly 1-index using the clock cycle)
cycle = 0
for ins in instructions:
  cycle += 1
  if cycle > 220:
    break

  X.append(X[-1]) # Replicate previous value

  if ins != "noop":
    X.append(X[-1] + int(ins[len("addx "):]))
    cycle += 1

sum_signals = X[20] * 20 + X[60] * 60 + X[100] * 100 + X[140] * 140 + X[180] * 180 + X[220] * 220
print(f"Sum of the signal strengths at cycles 20, 60, 100, 140, 180 and 220: {sum_signals}")
assert sum_signals == 13440
# Answer time: 15:13 (AoC time)

# DISCLAIMER:
# The original solution file was lost.
# This file re-creates the original solution as close as it is remembered and from shared snippets.
