//to reproduce, please download my GCJ framework http://github.com/dusek/gcj
//and place this file as problems/2009/round1C/A.py and run
//bin/solve.sh 2009.round1C A <your input file> > <your output file>
//I had problems uploading ZIP archive of the linked repository as source code
//to GCJ
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <iterator>
#include <gcj/Solvers.hpp>
#include <gcj/Cases.hpp>
#include <gcj/main.hpp>

class Case : public gcj::SingleLineCase {
    int m_solution;
    std::vector<std::vector<int> > a;
    std::vector<int> m_cell_length;
public:
    Case(int cells, int prisoners_to_release, std::istream& input)
        :
    a(prisoners_to_release+1)
    {
        std::vector<int>& a0=a[0];
        a0.resize(prisoners_to_release+1);
        int prev_cell, cell;
        cell=0;
        while (prisoners_to_release-- > 0) {
            prev_cell=cell;
            input >> cell;
            m_cell_length.push_back(cell - prev_cell - 1);
        }
        m_cell_length.push_back(cells - cell); // (cells+1) - cell - 1
    }

    virtual void solve() {
        const int max_l = a.size();
        for (int l = 0; l < max_l - 1; ++l) {
            //cell_length == l + 1
            const int size = a[l].size()-1;
            for (int i = 0; i < size; ++i) {
                // find minium division
                int min = -1;
                for (int k = 1; k <= l+1; ++k) {
                    int div_value = a[k-1][i] + a[l-k+1][i+k];
                    if ((min == -1) || (div_value < min))
                        min = div_value;
                }
                min += l;
                for (int k = 0; k < l+2; ++k) {
                    min += m_cell_length[i+k];
                }
                a[l+1].push_back(min);
            }
        }
        m_solution = a[a.size()-1][0];
    }

    virtual void output_only_solution_line(std::ostream& output) {
        output << m_solution;
    }
};

class Solver : public gcj::StandardSolver {
    virtual bool parallelize() const
    { return true; }

    virtual gcj::Case *parse_one_case(std::istream& input) {
        int cells, prisoners_to_release;
        input >> cells >> prisoners_to_release;
        return new Case(cells, prisoners_to_release, input);
    }
};

int main(int argc, char **argv) {
    Solver solver;
    return gcj::main(argc, argv, solver);
}
