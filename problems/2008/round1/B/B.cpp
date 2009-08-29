#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

int solve_one(std::istream &i);

enum {
    Go=0,
    Plus=1,
    Minus=2,
};

static const long long primes[] = {2,3,5,7};

int main (int argc, char *argv[]) {
    std::ifstream input(argv[1], std::ios_base::in);
    //std::stringstream input("4\n1\n9\n011\n12345");
    //std::ofstream output(argv[2], std::ios_base::out|std::ios_base::trunc);
    std::ostream &output = std::cout;

    int n;
    input >> n;
    for (int i=0; i<n; i++) {
        std::cerr << "Solving case " << i+1 << std::endl;
        output << "Case #" << i+1 << ": " << solve_one(input) << std::endl;
        output.flush();
    }
    //std::stringstream s("011");
    //std::cout << solve_one(s) << std::endl;

    return 0;
}

int solve_one(std::istream &input) {
    std::string number;
    input >> number;
    int n = number.size();
    if (n==1) {
        std::stringstream numstream(number);
        int number_value;
        numstream >> number_value;
        if (number_value==1)
            return 0;
        else
            return 1;
    }
    std::vector<int> signs(n-1, Go);
    int ugly=0;
    while (true) {
        int factor=1;
        int i=0;
        int j=0;
        long long sum = 0;
        for (int k=0; k<n-1; k++) {
            int sign=signs[k];
            j=k+1;
            if (sign==Go)
                continue;
            long long cut;
            std::stringstream number_portion(number.substr(i, j-i));
            number_portion >> cut;
            sum += factor * cut;
            if (sign==Plus)
                factor = 1;
            else
                factor = -1;
            i=j;
        }
        std::stringstream number_portion(number.substr(i));
        long long cut;
        number_portion >> cut;
        sum += factor * cut;
        if ((sum%2==0) || (sum%3==0) || (sum%5==0) || (sum%7==0)) {
            ugly++;
        }

        for (i=0; (i < n-1) && signs[i]==2; ++i)
            signs[i]=0;
        if (i==n-1)
            break;
        else
            signs[i]+=1;
    }
    return ugly;
}
