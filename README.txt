If you want to reproduce my solution from Google Code Jam, follow these
instructions (example follows; if you instead want to use this library to code your
own solutions, head to the QUICK START section):

0. Definitions:
<gcj-dir>: the root directory of the archive (the directory usually
named "gcj").
<input-file-name>: name of file which contains the small or large (or whatever) input to solve
<output-file-name>: name of file to which write solution

I also expect these instructions will be followed on a UNIX system. I do not
have the time to test on Windows, even though I tend to write multiplatform code.

1. Determine whether I used C++ or Python
  * look at problems/<year>/<round>/<problem>.<"py" or "cpp">. I use latin letters
    for the <problem> part.
2a. If I used Python (tested with 2.6.1):
2a1. Run <gcj-dir>/bin/solve.sh <year>.<round> <problem> <input-file-name> > <output-file-name>
     where the ">" sign between input and output file is shell's output redirection
2b. If I used C++ (tested on g++ 4.2.1):
2b1. compile the source code: g++ -I<gcj-dir>/include -o <problem> <gcj-dir>/<year>/<round>/<problem>.cpp
2b2. run the binary: ./<problem> <input-file-name> <output-file-name>

EXAMPLE:
========
You want to evaluate problem "C. Welcome to Code Jame" from Round 1A in year 2009.
So <year>=2009, <problem>=C

Python:
-------
cd <gcj-dir>
ls problems/2009 # you find out that "Round 1A" is represented by directory "round1A"
ls problems/2009/round1A # you find that only file there starting with "C" is "C.py"
bin/solve.sh 2009.round1A C C-large.in.txt > C-large.out.txt

C++:
----
cd <gcj-dir>
ls problems/2009 # you find out that "Round 1A" is represented by directory "round1A"
ls problems/2009/round1A # you find that only file there starting with "C" is "C.cpp"
g++ -I./include -O2 -o C problems/2009/round1A/C.cpp
./C C-large.in.txt C-large.out.txt


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
