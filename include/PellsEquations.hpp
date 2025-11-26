#pragma once

#include "QuadraticIrrationals.hpp"
#include <optional>

class PellsEquations{
private:
    QuadraticIrrationals alpha;
    std::optional<std::pair<long long, long long>> FundSolutions;
    int _n;
    bool isPerfectSquare(long long n) {
        if (n < 0) return false; 
        long long root = static_cast<long long>(std::sqrt(n));
        return root * root == n;
    }
public:
    PellsEquations(int D, int n);

    std::pair<long long, long long> FundamentalSolutions();
    std::pair<long long, long long> jSolutions(long long j);

    std::pair<long long, long long> FundSolNonForm();
    std::pair<long long, long long> jSolNonForm(int j);
};
