#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <iterator>
#include <gcj/Solvers.hpp>
#include <gcj/Cases.hpp>
#include <gcj/main.hpp>

class Case : public gcj::SingleLineCase {
    const std::string m_hay;
    const std::string& m_needle;
    std::size_t m_solution;
public:
    Case(const std::string& hay, const std::string& needle)
        : m_hay(hay), m_needle(needle), m_solution(0)
    {}

    virtual void solve() {
        std::vector<int> score(m_hay.size(), 1);
        std::for_each(m_needle.begin(), m_needle.end(), letter_advancer(score, m_hay));
        m_solution = *(--score.end());
    }

    virtual void output_only_solution_line(std::ostream& o) {
        o.width(4);
        o.fill('0');
        o << m_solution;
    }

private:
    struct letter_advancer : public std::unary_function<char, void> {
        std::vector<int>& m_score;
        const std::string& m_hay;
        bool m_first;

    public:
        letter_advancer(std::vector<int>& score, const std::string& hay)
            : m_score(score), m_hay(hay), m_first(true)
        {}

        void operator()(char needle_char) {
            //std::clog << "Advancing on letter " << needle_char << ": ";
            //std::copy(m_score.begin(), m_score.end(), std::ostream_iterator<int>(std::clog, " "));
            //std::clog << std::endl;
            std::for_each(m_hay.begin(), m_hay.end(), step_performer(needle_char, m_score, m_first));
            m_first = false;
        }
    };

    struct step_performer : public std::unary_function<char, void> {
        const char m_needle_char;
        std::vector<int>::iterator m_score_it;
        std::size_t m_prev;
        std::size_t m_sum;
    public:
        step_performer(char needle_char, std::vector<int>& score, bool first)
            : m_needle_char(needle_char), m_score_it(score.begin()), m_prev(first ? 1 : 0), m_sum(0)
        {}

        void operator()(char hay_char) {
            if (hay_char == m_needle_char) {
                m_sum += m_prev;
                m_sum %= 10000;
            }
            m_prev = *m_score_it;
            *m_score_it = m_sum;
            ++m_score_it;
        }
    };
};

class Solver : public gcj::StandardSolver {
private:
    const static std::string needle;
public:
    virtual bool parallelize() const
    { return true; }

    virtual gcj::Case *parse_one_case(std::istream& i) {
        std::string hay;
        std::getline(i, hay);
        const std::string& needle = Solver::needle;
        return new Case(hay, needle);
    }

};
const std::string Solver::needle = "welcome to code jam";

int main(int argc, char **argv) {
    Solver solver;
    gcj::main(argc, argv, solver);
}
