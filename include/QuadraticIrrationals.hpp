#pragma once

#include <cmath>
#include <vector>
#include <gmpxx.h>


class QuadraticIrrationals {
private:
    long long p;
    long long Q;
    long long D;

    static long long isqrt(long long x) {
        return static_cast<long long>(std::floor(std::sqrt(x)));
    }

public:
    QuadraticIrrationals(long long p_, long long Q_, long long D_);

    inline int GetD(){
        return D;
    }

    int period_right();
    mpz_class periodD(); 
    std::vector<long long> periodic_continued_fraction(int number);
    static std::vector<double> averaging(const std::vector<long long>& array);

    static void periods_and_averaging(std::vector<long long> &a, std::vector<mpz_class> &b,
                           std::vector<mpq_class> &c, 
                           size_t maxD, int p, int Q);
};