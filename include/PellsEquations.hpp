#pragma once

#include "QuadraticIrrationals.hpp"
#include <optional>

class PellsEquations{
private:
    QuadraticIrrationals alpha;
    std::optional<std::pair<mpz_class, mpz_class>> FundSolutions;
    long long _n;
    bool isPerfectSquare(const mpz_class& n) {
        return mpz_perfect_square_p(n.get_mpz_t()) != 0;
    }

public:
    PellsEquations(long long D, long long n);

    std::pair<mpz_class, mpz_class> FundamentalSolutions();
    std::pair<mpz_class, mpz_class> jSolutions(long long j);

    std::pair<mpz_class, mpz_class> FundSolNonForm();
    std::pair<mpz_class, mpz_class> jSolNonForm(int j);
};
