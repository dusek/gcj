#ifndef GCJ_CASES_HPP_
#define GCJ_CASES_HPP_

#include <ostream>
#include <gcj/Solver.h>

namespace gcj {
class MultiLineCase : public Case {
public:
    virtual void output_solution(std::ostream& o, std::size_t cur_idx) {
        o << "Case #" << cur_idx + 1 << ":";
        output_only_solution(o);
    }
protected:
    virtual void output_only_solution(std::ostream& o) = 0;
};

class SingleLineCase : public MultiLineCase {
public:
    virtual void output_only_solution(std::ostream& o) {
        o << " ";
        output_only_solution_line(o);
        o << std::endl;
    }

protected:
    virtual void output_only_solution_line(std::ostream& o) = 0;
};
}

#endif

