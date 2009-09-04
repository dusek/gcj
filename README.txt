QUICK START:

The demo files and demo input is in directory problems/demo.

a. If you are using Python
==========================
1. write your solution in the appropriate subdirectory of "problems" directory
   - in that solution .py file, import gcj and inherit Solver from gcj.Solver;
     override _solve_one(self) method which parses one case and returns string
     with solution
2. run bin/solve.sh <path/to/solution/file> <solution file name without .py> <input file>
NOTE: don't worry about the "Solving case <case_number>" messages,
      they are sent to stderr, if you redirect output to a file (that you will be submitting),
      the messages will still be shown to you and not written to the file

EXAMPLE:
a solver which outputs true/false based on whether input is even

problems/2009/round0/C.py:

import gcj
class Solver(gcj.Solver):
    def _solve_one(self):
        i = self._getintline()
        return str(i % 2 == 0).lower()

from anywhere run with:

/path/to/bin/solve.sh 2009.round0 C C-large.in.txt > C-large.out.txt

b. If you are using C++
=======================
1. write your solution anywhere into a .cpp file.
   - implement Solver and Case interfaces, typically by implementing
     StandardSolver from <gcj/Solvers.hpp> and SingleLineCase from <gcj/Cases.hpp>
   - in your main, create your Solver class and return gcj::main(argc, argv, <the_solver_you_created>
2. compile
   - if you want parallel execution and have Intel's TBB installed
       g++ -Wall -O2 -DGCJ_PARALLELIZE -I<path/to/gcj/root>/include -o C C.cpp -ltbb
   - otherwise omit the "-DGCJ_PARALLELIZE" and "-ltbb":
       g++ -Wall -O2 -I<path/to/gcj/root>/include -o C C.cpp
3. run
   - ./C <input file> <output file>
   - or to send output to stdout, omit <output file>: ./C <input file>

EXAMPLE:
a solver which outputs true/false based on whether input is even

1. problems/demo/C.cpp:

#include <ios>
#include <gcj/Solvers.hpp>
#include <gcj/Cases.hpp>
#include <gcj/main.hpp>

class Case : public gcj::SingleLineCase {
    int m_number;
    bool m_result;
public:
    explicit Case(int number) : m_number(number) {}
    virtual void solve()
    { m_result = ((m_number % 2) == 0); }
    virtual void output_only_solution_line(std::ostream& output)
    { output << std::boolalpha << m_result; }
};

class Solver : public gcj::StandardSolver {
public:
    virtual bool parallelize() const
    { return true; } // or return false if you are not thread-safe

    virtual gcj::Case *parse_one_case(std::istream& input) {
        int number;
        input >> number;
        return new Case(number);
    }
};

int main(int argc, char **argv) {
    Solver solver;
    return gcj::main(argc, argv, solver);
}

2. then compile:
g++ -Wall -O2 -DGCJ_PARALLELIZE -I$HOME/Documents/gcj/include -o C C.cpp -ltbb

3. then run:
./C C-large-in.txt C-large-out.txt

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
