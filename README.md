# Advent of Code 2022
My solutions to 2022's [Advent of Code](https://adventofcode.com/2022/about).

Each day has its own `README.md` file with the corresponding puzzle's description, automatically transformed into markdown, to ease the remembering and understanding of the solutions. Obviously, the creator of these puzzles and descriptions is [Eric Wastl](https://twitter.com/ericwastl).

Each program responsible for solving a specific puzzle also checks that the computed solution is my own correct solution to that puzzle (which is hardcoded into the source code after solving the puzzle). This check is performed by means of an `assert` in the last (or second to last, if there's an `exit()`) line executed in the program. The programs also have some commented-out debug lines, or other explanations, to give some insight about how their development process went.

There were no specific objectives set for the solutions' code in terms of execution time, memory or code quality optimizations (aside from making a program that computes the solution in a reasonable amount of time, say, up to 15 minutes).

This year I had no intentions of waking up at 5:50 a.m. for 25 consecutive days to achieve leaderboard-competitive times. However, I decided to time myself when coding the solutions, if coded in one sitting, so I could have a way to track and compare my performance. I timed myself using my phone's chronometer app, and also Advent of Code's tracker the few days I was awake at the time the puzzle unlocked. When using my chronometer, time for part 1 started whenever I clicked the link to enter the specific puzzle's page (description); and time for part 2 started whenever I clicked "Continue to part two" after giving a correct solution for part 1. On the last lines of the programs a comment with the noted times is provided: _Answer time_ is the time it took me to solve that specific part of the corresponding puzzle. In part 2 programs, _Total day time_ is the sum of the part 1 and 2 Answer times (i.e. time from clicking the link to enter the puzzle's page, until clicking "Submit" for part 2 and receiving confirmation that it is a correct solution). Times that were noted using AoC's tracker instead of my chronometer are explicitly specified as so (e.g. saying _(AoC time)_). As my phone broke on December the 20th and the last days of the AoC I wasn't awake by the time the puzzles unlocked, the very last puzzles were not timed.

Also on the last lines of the programs, before the noted solution times, a comment with _Fails_ might be provided. These indicated the amount of times an incorrect answer for that specific part of the puzzle was submitted to AoC before the correct one (if greater than 0).

Some days provide multiple solutions. "_first_" solutions are the programs that provided the correct answer for that part, as unoptimized, spaghetti, or even incorrect as they might be. The "regular" solutions improve these programs in one or more of the stated aspects.

This year the repository doesn't include my input files, as I was told by a friend that it is recommended not to make your inputs public so that the input generator doesn't get reverse-engineered (as crazy as that sounds).

## Trivia and other notes
This was the very first year that I managed to keep up with the days; i.e. I solved both parts of each day before the next day was unlocked. I officially properly completed AoC and now I can retire.

My favourite AoC 2022 day was 21.

The days I liked the least were 19 and 16 (in that order).

My solutions for both parts of day 16 are technically wrong; however, they provide the correct solution for all the tested inputs. They are, anyway, very slow programs (6.5 minutes of execution time for part 2). A more in-depth explanation is provided in part 1's code, as a comment. A correct, more optimized version of the solutions is WIP, and probably will be for ever.