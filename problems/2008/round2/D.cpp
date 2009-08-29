#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include <cstdlib>

static int solve(int k, const std::string &input);
static void solve_one(std::istream &i, std::ostream &o);

int main(int argc, char **argv) {
    if (argc != 2)
        return ::EXIT_FAILURE;
    std::fstream input(argv[1], std::ios_base::in);
    std::ostream &output = std::cout;

    int N;
    input >> N;
    for (int i = 1; i <= N; i++) {
        std::cerr << "Solving case " << i << std::endl;
        output << "Case #" << i << ": ";
        solve_one(input, output);
        output << std::endl;
    }
    //input and output will get closed by their destructors
    return ::EXIT_SUCCESS;
}

static void solve_one(std::istream &i, std::ostream &o) {
    int k;
    i >> k;
    std::string input;
    i >> input;
    int answer = solve(k, input);
    o << answer;
}

static int solve(int k, const std::string &input) {
    std::vector<int> p;
    p.reserve(k);
    for (int i = 0; i < k; i++) {
        p.push_back(i);
    }
    std::string mod(input);
    int L = input.size();
    int min = -1;
    do {
        int offset = 0;
        for (int offset = 0; offset < L; offset += k) {
            for (int j = 0; j < k; j++)
                mod[offset + j] = input[offset + p[j]];
        }
        std::string::iterator unique_end = std::unique(mod.begin(), mod.end());
        int uniques = unique_end - mod.begin();
        if ((min == -1) || (min > uniques))
            min = uniques;
    } while (std::next_permutation(p.begin(), p.end()));

    return min;
}
