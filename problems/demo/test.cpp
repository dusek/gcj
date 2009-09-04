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
