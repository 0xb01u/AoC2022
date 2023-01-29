from bs4 import BeautifulSoup as bs
from datetime import date
from sys import argv
from os import system, path, mkdir
import requests as req
import re

year, month, days = date.today().timetuple()[:3]
x = "py"

options = str(argv).replace("'", "").replace(",", "")[1:-1]

if " -d" in options:
	days = options.split(" -d ")[1].split(" ")[0]
	if "-" in days:
		days = list(range(int(days.split("-")[0]), int(days.split("-")[1]) + 1))
	else:
		days = [int(days)]
else:
	days = [int(days)]

if " -y" in options:
	year = int(options.split(" -y ")[1].split(" ")[0])

if " -x" in options:
	x = options.split(" -x ")[1].split(" ")[0]

for day in days:

	page = f"https://adventofcode.com/{year}/day/{day}"
	session = {"session": open("session").read()}

	if not path.exists(f"./{day:02d}"):
		print(f"Creating directory for day {day:02d}")
		mkdir(f"./{day:02d}")

	if not path.exists(f"./{day:02d}/input.txt"):
		print(f"Fetching input for day {day:02d}")
		day_input = req.get(
			f"{page}/input",
			cookies=session
		).text

		input_txt = open(f"./{day:02d}/input.txt", "w")
		input_txt.write(day_input)
		input_txt.close()

	if not path.exists(f"./{day:02d}/README.md") or " -md" in options:
		print(f"Fetching description for day {day:02d}")
		description = str(bs(req.get(
			page,
			cookies=session
			).text, "html.parser").find("main"))
		description_md = re.sub(r'</?main>', "", description)
		description_md = re.sub(r'<script.*?/script>', "", description_md)
		description_md = re.sub(r'</?em.*?>', "**", description_md)
		description_md = re.sub(r'(<pre><code>)|(^</code></pre>)', "```\n", description_md)
		description_md = re.sub(r'(<pre><code>)|(</code></pre>)', "\n```\n", description_md)
		description_md = re.sub(r'</?code(.*?)>', "`", description_md)
		description_md = re.sub(r'</?p>', "\n", description_md)
		description_md = re.sub(r'<span.*?>', "", description_md)
		description_md = re.sub(r'</span>', "", description_md)
		description_md = re.sub(r'</?ul>', "", description_md)
		description_md = re.sub(r'<li>', " - ", description_md)
		description_md = re.sub(r'</li>', "", description_md)
		description_md = re.sub(r'</?p.*?>', "\n", description_md)
		description_md = re.sub(r'<h2.*?>', "## ", description_md)
		description_md = re.sub(r'</h2>', "", description_md)
		description_md = re.sub(r'<article.*?>', "", description_md)
		description_md = re.sub(r'</article>', "", description_md)
		# 2021 day 10 uses "](" as valid substring in input examples. We exclude it from being treated as a markdown link by temporally using "__aocTool_parser_IR__".
		description_md = re.sub(r'<a href="(.*?)".*>(.*?)</a>', r'[\2__aocTool_parser_IR__](\1)', description_md)
		description_md = re.sub(r'<form(.|\n)*?/form>', "", description_md)
		description_md = re.sub(r'__aocTool_parser_IR__\]\(/', r'](https://adventofcode.com/', description_md)
		description_md = re.sub(r'__aocTool_parser_IR__\]\(([^/h])', rf'](https://adventofcode.com/{year}/day/\1', description_md) # 'h' for https; for wikipedia links etc
		description_md = re.sub(r'__aocTool_parser_IR__', "", description_md)
		description_md = re.sub(r'`\*\*(.*)\*\*`', r'**`\1`**', description_md)	# Correct bold code
		description_md = re.sub(r'\n\n', "\n", description_md)
		description_md = re.sub(r'\nYou can also.*', "", description_md, flags=re.S)
		description_md = re.sub(r'&gt;', ">", description_md)
		description_md = re.sub(r'&lt;', "<", description_md)
		description_md = re.sub(r'<style>.*</style>', "", description_md)

		open(f"./{day:02d}/README.md", "w").write(description_md)

	if not path.exists(f"./{day:02d}/one.{x}"):
		print(f"Creating {day:02d}/one.{x}")
		file = open(f"./{day:02d}/one.{x}", "w")
		if x == "py":
			file.write(f'# --- Advent of code {year}: Day {day:02d} ---\n\n# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)\n\ninp = open("input.txt").read().splitlines()\n\n')
		elif x == "lua":
			file.write(f"-- --- Advent of code {year}: Day {day:02d} ---\n\n-- (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2022.)\n\npackage.path = package.path .. \";../modules/?.lua\"\nlocal tools = require \"tools\"\n\ninput = tools.readlines(\"input.txt\")\n\n")
		file.close()

if " -g" in options:
	msg = f"Day " + str(days)[1:-1]

	if " -m" in options:
		msg = options.split("-m ")[1]

	system("git add -A")
	system(f"git commit -m \"Automatic aocTool commit: \'{msg}\'\"")
	system("git push origin main")
