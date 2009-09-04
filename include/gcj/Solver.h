#ifndef GCJ_SOLVER_H_
#define GCJ_SOLVER_H_

#include <cstddef>
#include <iosfwd>

namespace gcj {

class Case {
public:
    /**
     * Solves the case and stores the solution internally
     */
    virtual void solve() = 0;

    /**
     * Formats textual solution description to output
     * @param o - stream into which format the solution
     * @param cur_idx - position of this case in list of all cases (from 0)
     */
    virtual void output_solution(std::ostream& o, std::size_t cur_idx) = 0;
};

class Solver {
public:
    /**
     * Parses input file portion preceding tasks.
     * @param i - input stream where header is located
     * @return Number of cases in the input file
     */
    virtual std::size_t parse_header(std::istream& i) = 0;
    /**
     * Parses single case definition to a Case object
     * @param i - input strean where cases description is located
     */
    virtual Case *parse_one_case(std::istream& i) = 0;
    /**
     * Query solver whether it is thread-safe
     */
    virtual bool parallelize() const = 0 ;
};
}

#endif

