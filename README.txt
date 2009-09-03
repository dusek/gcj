For Google Code Jam, I use a custom "gcj" library to ease the task of
reading input and producing output. I am submitting the library along
with code solving the problem.

Each problem is solved in directory gcj/problems/<year>/round<N>/<ABC>/<problem-letter>.py,
where <N> is the number of round (i.e. for "Round 1", N=1), <ABC> is present
only for Round 1 and denotes whether the problem is from Round 1A, or Round 1B
or Round 1c. Finally, <problem-name> is either "A" or "B" or "C", corresponding
to the problem letter in original problem statement.

TO REPRODUCE THE SUBMITTED OUTPUT:
==================================

Run this command on UNIX (use the ".<ABC>" part only for Round 1):
gcj/bin/solve round<N>.<ABC> <problem-letter> <testcase-input-file-path>

I.e., to solve problem B from Round 1C in year 2008, run:
gcj/bin/solve 2009.round1.C B <testcase-input-file-path>

To solve problem A from Round 3 in year 2009, run:
gcj/bin/solve 2009.round3 A <testcase-input-file-path>



Sorry for any inconvenience with my setup.
