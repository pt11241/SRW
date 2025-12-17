#include "../include/PellsEquations.hpp"
#include <iostream>
#include <gmpxx.h>



mpz_class nod(const mpz_class& a1, const mpz_class& b1) {
    mpz_class g;
    mpz_gcd(g.get_mpz_t(), a1.get_mpz_t(), b1.get_mpz_t());
    return g;
}


mpf_class pow_mpf(const mpf_class& base, unsigned long exp){
    mpf_class result;
    mpf_pow_ui(result.get_mpf_t(), base.get_mpf_t(), exp);
    return result;
}



PellsEquations::PellsEquations(long long D, long long n) : alpha(0, 1, D), _n(n){}

std::pair<mpz_class, mpz_class> PellsEquations::FundamentalSolutions(){ // fund solution of x^2 - D*y^2 = +-1
    if(FundSolutions)                                   
        return {FundSolutions->first, FundSolutions->second};
    long long n = _n;
    if(!(_n == 1 || _n == -1)){
        n = 1;
    }
    int period = alpha.period_right();
    std::vector<long long> pqf;
    if(n == 1){
        if(period % 2 == 0){
            pqf = alpha.periodic_continued_fraction(period);        
        }else{
            pqf = alpha.periodic_continued_fraction(2*period);
        }
    }else if(n == -1){
        if (period % 2 == 0){
            std::cout << "The positive solutions of x^2 - Dy^2 = -1 are nonexistent when period is even";
            return {};
        }else{
            pqf = alpha.periodic_continued_fraction(period);
        }
    }
    // std::cout << "here 1" << '\n';
    // std::cout << period << '\n';
    long count = 0;
    mpz_class a_2 = 0, a_1 = 1;
    mpz_class b_2 = 1, b_1 = 0;
    for(auto q : pqf){
        count++;
        // std::cout << period << '\n';
        mpz_class q_mpz(static_cast<unsigned long>(q));
        mpz_class new_a_1 = q_mpz * a_1 + a_2;
        mpz_class new_b_1 = q_mpz * b_1 + b_2;
        a_2 = a_1;
        a_1 = new_a_1;
        b_2 = b_1;
        b_1 = new_b_1;
    }
    FundSolutions = {a_1, b_1};
    return {a_1, b_1};
}

std::pair<mpz_class, mpz_class> PellsEquations::jSolutions(long long j){
    auto [x1, y1] = FundamentalSolutions();
    mpf_class sqrtD(alpha.GetD(), 256); // high precision sqrt
    mpf_class base = mpf_class(x1) + mpf_class(y1) * sqrtD;
    mpf_class base_conj = mpf_class(x1) - mpf_class(y1) * sqrtD;

    mpf_class base_pow   = pow_mpf(base, j);
    mpf_class base_conj_pow = pow_mpf(base_conj, j);

    mpf_class x = (base_pow + base_conj_pow) / 2;
    mpf_class y = (base_pow - base_conj_pow) / (2 * sqrtD);


    return {mpz_class(x), mpz_class(y)};
}

std::pair<mpz_class, mpz_class> PellsEquations::FundSolNonForm(){
    auto [xFund, yFund] = FundamentalSolutions();
    mpz_class boundsY, y;
    if (_n > 1){
        mpf_class boundCalc = mpf_class(yFund) * sqrt(_n) / sqrt(2 * xFund);
        boundsY = ceil(boundCalc);
        y = 0;
    }else if(_n < -1){
        mpf_class boundCalc = mpf_class(yFund) * sqrt(std::abs(_n)) / sqrt(2 * (xFund - 1));
        boundsY = ceil(boundCalc);
        y = 1;
    }else{
        std::cout << "_n must be > 1 or < -1\n";
        return {};
    }
    
    for (; y <= boundsY; y++){
        mpz_class x2 = alpha.GetD() * y * y + mpz_class(static_cast<int>(_n));
        if (isPerfectSquare(x2)){ // нужно переписать isPerfectSquare под mpz_class
            mpz_class x;
            mpz_sqrt(x.get_mpz_t(), x2.get_mpz_t());
            if (nod(x, y) == 1)
                return {x, y};
        }
    }
    std::cout << "No integer solutions\n";
    return {};
}

std::pair<mpz_class, mpz_class> PellsEquations::jSolNonForm(int j){
    auto [x1, y1] = FundSolNonForm();
    auto [u, v] = jSolutions(j);
    mpz_class X = u * x1 + v * y1 * alpha.GetD();
    mpz_class Y = u * y1 + v * x1;
    return {X, Y};
}