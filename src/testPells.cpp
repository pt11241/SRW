#include "../include/PellsEquations.hpp"
#include <iostream>


int main(){
    int D1 = 425, n1 = -1;
    PellsEquations equation1(D1, n1); 
    std::pair<long long, long long> sol1 = equation1.FundamentalSolutions();
    std::pair<long long, long long> jsol1 = equation1.jSolutions(2);
    std::cout << sol1.first << ' ' << sol1.second << '\n';
    std::cout << jsol1.first << ' ' << jsol1.second << '\n';

    int D2 = 13, n2 = -27;
    PellsEquations equation2(D2, n2);
    std::pair<long long, long long> sol2 = equation2.FundSolNonForm();
    std::pair<long long, long long> jsol2 = equation2.jSolNonForm(1);
    std::cout << sol2.first << ' ' << sol2.second << '\n';
    std::cout << jsol2.first << ' ' << jsol2.second << '\n';

    int D3 = 3, n3 = 13;
    PellsEquations equation3(D3, n3);
    std::pair<long long, long long> sol3 = equation3.FundSolNonForm();
    std::pair<long long, long long> jsol3 = equation3.jSolNonForm(1);
    std::cout << sol3.first << ' ' << sol3.second << '\n';
    std::cout << jsol3.first << ' ' << jsol3.second << '\n';
    

    return 0;
}