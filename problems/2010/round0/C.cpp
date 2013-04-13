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
    const int m_rides;
    const int m_ride_size;
    const int m_ngrp;
    const std::vector<int> m_group_sizes;
    std::vector<int> m_group_next_idx;
    std::vector<int> m_group_next_sum;
public:
    Case(int rides, int ride_size, int ngrp, const std::vector<int>& group_sizes)
        : m_rides(rides), m_ride_size(ride_size), m_ngrp(ngrp), m_group_sizes(group_sizes),
          m_group_next_idx(m_group_sizes.size(), -1), m_group_next_sum(m_group_sizes.size(), -1)
    {
        std::clog << "Created case with:" << std::endl;
        std::clog << "  rides = " << rides << std::endl;
        std::clog << "  ride_size = " << ride_size << std::endl;
        std::clog << "  ngrp = " << ngrp << std::endl;
        std::clog << "  group_sizes = ";
        std::copy(m_group_sizes.begin(), m_group_sizes.end(), std::ostream_iterator<int>(std::clog, " "));
        std::clog << std::endl;
    }

    virtual void solve() {
        int pos, rides, money, reach_rides, reach_money;
        std::clog << "Finding cycle" << std::endl;
        find_cycle(pos, rides, money, reach_rides, reach_money);
        std::clog << "Cycle found: pos = " << pos << ", rides = " << rides << ", money = " << money << ", reach_rides = " << reach_rides << ", reach_money = " << reach_money << std::endl;
        m_solution = reach_money;
        if (m_rides > reach_rides) {
            int repeats = (m_rides - reach_rides) / rides;
            int remainder = (m_rides - reach_rides) % rides;
            m_solution += repeats*money;
            while (remainder--) {
                m_solution += m_group_next_sum[pos];
                pos = m_group_next_idx[pos];
            }
        }
    }

    virtual void output_only_solution_line(std::ostream& o) {
        o << m_solution;
    }

private:
    void find_cycle(int& pos, int& rides, int& money, int& reach_rides, int& reach_money) {
        int i = 0;
        int total_rides = 0;
        int total_money = 0;
        while (m_group_next_idx[i] == -1) {
            std::clog << "i = " << i << std::endl;
            int size = 0;
            int idx = i;
            while (size + m_group_sizes[idx] <= m_ride_size) {
                std::cerr << " size = " << size << ", idx = " << idx << ", group_size = " << m_group_sizes[idx] << std::endl;
                size += m_group_sizes[idx];
                idx++;
                if (idx >= m_ngrp)
                    idx -= m_ngrp;
            }
            m_group_next_idx[i] = idx;
            m_group_next_sum[i] = size;
            i = idx;
            total_money += size;
            ++total_rides;
        }
        pos = i;

        reach_rides = 0;
        reach_money = 0;
        i = 0;
        while ((i != pos) && (reach_rides < m_rides)) {
            reach_rides++;
            reach_money += m_group_next_sum[i];
            i += m_group_next_idx[i];
        }
        
        rides = total_rides - reach_rides;
        money = total_money - reach_money;
    }
};

class Solver : public gcj::StandardSolver {
public:
    virtual bool parallelize() const
    { return true; }

    virtual gcj::Case *parse_one_case(std::istream& i) {
        std::string dummy_string;
        int rides, ride_size, nGroup;
        std::vector<int> group_sizes;

        i >> rides;
        i >> ride_size;
        i >> nGroup;
        for (int j = 0; j < nGroup; ++j) {
            int group_size;
            i >> group_size;
            group_sizes.push_back(group_size);
        }

        return new Case(rides, ride_size, nGroup, group_sizes);
    }

};

int main(int argc, char **argv) {
    Solver solver;
    gcj::main(argc, argv, solver);
}
