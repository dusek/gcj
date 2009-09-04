#include <string>
#include <istream>
#include <gcj/Solver.h>

namespace gcj {

class StandardSolver : public Solver {
public:
    virtual std::size_t parse_header(std::istream& i) {
        std::size_t case_count;
        i >> case_count;
        std::string dummy_line_end;
        std::getline(i, dummy_line_end);
        return case_count;
    }
};

}
