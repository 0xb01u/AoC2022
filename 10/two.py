# --- Advent of code 2022: Day 10 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)

instructions = open("input.txt").read().splitlines()

msg = ""
X = [0, 1] # Values of register X over time (0 added to correctly 1-index using the clock cycle)
cycle = 0
for ins in instructions:
  cycle += 1
  if cycle > 6 * 40:
    break

  if abs((cycle - 1) % 40 - X[-1]) < 2:
    msg += "#"
  else:
    msg += " "

  X.append(X[-1]) # Replicate previous value

  if ins != "noop":
    cycle += 1

    if abs((cycle - 1) % 40 - X[-1]) < 2:
      msg += "#"
    else:
      msg += " "

    X.append(X[-1] + int(ins[len("addx "):]))

print("Eight capital letters written on the CRT:\n")
for i in range(6):
	print(msg[i * 40:(i + 1) * 40])
# At first I didn't implement correctly this solver program, but the
# printed message was clear enough to understand what the solution was.
# The program has been modified to correctly display the solution
# for completion and presentation purposes.
assert msg == "\
###  ###  ####  ##  ###   ##  ####  ##  \
#  # #  #    # #  # #  # #  #    # #  # \
#  # ###    #  #    #  # #  #   #  #  # \
###  #  #  #   # ## ###  ####  #   #### \
#    #  # #    #  # # #  #  # #    #  # \
#    ###  ####  ### #  # #  # #### #  # "
# Answer time: 11:42 (AoC time)
# Total day time: 26:55 (AoC time)

# DISCLAIMER:
# The original solution file was lost.
# This file re-creates the original solution as close as it is remembered and from shared snippets.
