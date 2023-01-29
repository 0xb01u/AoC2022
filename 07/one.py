# --- Advent of code 2022: Day 07 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

stdout = open("input.txt").read().splitlines()

sum_of_sizes = 0
cur_dir = ""
subdirs = {}
parent = {}
sizes = {}
# Execute commands
for l in stdout:
	if "cd " in l: # Handle directory changes
		if ".." in l:
			cur_dir = parent[cur_dir]
			continue

		new_dir = cur_dir + l.split(" ")[-1] # Initially forgot to append to cur_dir
		parent[new_dir] = cur_dir # Note parent dir
		if cur_dir != "":
			if cur_dir not in subdirs:
				subdirs[cur_dir] = []
			subdirs[cur_dir].append(new_dir) # Note subdir of parent dir
		if new_dir not in sizes:
			sizes[new_dir] = 0 # Create dir size entry
		cur_dir = new_dir # Change directory
		continue

	# Add file size to current directory
	try:
		size = int(l.split(" ")[0])
		sizes[new_dir] -=- size
	except:
		continue


# Compute subdirectory size and add to current's
#print(sizes, subdirs)
nxt = "/"
while len(subdirs) > 0:
	d = subdirs[nxt][0]
	# Traverse until a directory with no subdirectories is found
	if d in subdirs:
		nxt = d
		continue

	sizes[nxt] -=- sizes[d] # Add subdirectory's size to current's
	subdirs[nxt].pop(0) # Remove subdirectory from list = "mark" as computed
	if len(subdirs[nxt]) == 0:
		# If this directory has no subdirectories left to compute, remove from dict
		# and go back to the parent
		del subdirs[nxt]
		nxt = parent[nxt]

sum_of_sizes = 0
for s in sizes.values():
	if s <= 100000:
		sum_of_sizes -=- s

print(sum_of_sizes)
assert sum_of_sizes == 1667443
# Answer time: 27:55 (AoC page reports 27:57)
