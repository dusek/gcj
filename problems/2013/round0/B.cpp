#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <iterator>
#include <gcj/Solvers.hpp>
#include <gcj/Cases.hpp>
#include <gcj/main.hpp>

class Case : public gcj::SingleLineCase {
    bool m_possible;
    int N, M;
    int *m_lawn;
public:
    Case(int N, int M, int *lawn)
        :
        N(N), M(M), m_possible(false), m_lawn(lawn)
    {
    }

    virtual void solve() {
        int *test_lawn = new int[N*M];
        int64_t i;
        const int64_t P = 1 << (N+M);
        for (int64_t p = 0; p < P; ++p) {
            for (i = 0; i < N*M; ++i)
                test_lawn[i] = 2;
            for (i = 0; i < N+M; ++i) {
                if (p & (1 << i)) {
                    int offset;
                    int stride;
                    int count;
                    if (i < N) {
                        offset = i*M;
                        stride = 1;
                        count = M;
                    } else {
                        offset = i - N;
                        stride = M;
                        count = N;
                    }
                    for (int j = offset, c = 0; c < count; j += stride, ++c) {
                        if (test_lawn[j]==2)
                            test_lawn[j] = 1;
                    }
                }
            }
            if (std::equal(m_lawn, m_lawn+N*M, test_lawn))
            {
                m_possible = true;
                break;
            }
        }
    }

    virtual void output_only_solution_line(std::ostream& output) {
        if (m_possible)
            output << "YES";
        else
            output << "NO";
        //delete[] m_lawn;
    }
};

class Solver : public gcj::StandardSolver {
    virtual bool parallelize() const
    { return true; }

    virtual gcj::Case *parse_one_case(std::istream& input) {
        int N, M;
        input >> N >> M;
        int *lawn = new int[N*M];
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                int h;
                input >> h;
                //std::cerr << "(" << i << ", " << j << ") = " << h << std::endl;
                lawn[N*i + j] = h;
            }
        }
        return new Case(N, M, lawn);
    }
};

int main(int argc, char **argv) {
    Solver solver;
    return gcj::main(argc, argv, solver);
}
