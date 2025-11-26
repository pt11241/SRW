#include "../include/PellsEquations.hpp"
#include <iostream>



int nod(int a1, int b1){
    int a = a1, b = b1;
    while(b != 0){
        int bcopy = b;
        b = a % b;
        a = bcopy;
    }
    return a;
}



PellsEquations::PellsEquations(int D, int n) : alpha(0, 1, D), _n(n){}

std::pair<long long, long long> PellsEquations::FundamentalSolutions(){ // fund solution of x^2 - D*y^2 = +-1
    if(FundSolutions)                                   
        return {FundSolutions->first, FundSolutions->second};
    int n = _n;
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
    long long a_2 = 0, a_1 = 1;
    long long b_2 = 1, b_1 = 0;
    for(auto q : pqf){
        long long q_mpz = q;
        long long new_a_1 = q_mpz * a_1 + a_2;
        long long new_b_1 = q_mpz * b_1 + b_2;
        a_2 = a_1;
        a_1 = new_a_1;
        b_2 = b_1;
        b_1 = new_b_1;
    }
    FundSolutions = {a_1, b_1};
    return {a_1, b_1};
}

std::pair<long long, long long> PellsEquations::jSolutions(long long j){
    std::pair<long long, long long> fundsol = FundamentalSolutions();
    long long x1 = fundsol.first, y1 = fundsol.second; 
    
    long double base = x1 + y1 * std::sqrt((long double)alpha.GetD());
    long double base_conj= x1 - y1 * std::sqrt((long double)alpha.GetD());
    long double x = (std::pow(base, j) + std::pow(base_conj, j)) / 2.0;
    long double y = (std::pow(base, j) - std::pow(base_conj, j)) / (2.0 * std::sqrt((long double)alpha.GetD()));
    return {x, y};
}

std::pair<long long, long long> PellsEquations::FundSolNonForm(){
    std::pair<long long, long long> FundSol = FundamentalSolutions();
    long long boundsY = 0;
    long long y = 0;
    if (_n > 1){
        boundsY = std::ceil((FundSol.second * std::sqrt(_n)) / std::sqrt(2 * FundSol.first));
        y = 0;
    }else if(_n < -1){
        boundsY = std::ceil((FundSol.second * std::sqrt(std::abs(_n))) / std::sqrt(2 * (FundSol.first - 1)));
        y = 1;
    }else{
        std::cout << "_n must be > 1 or < -1" << '\n';
        return {};
    }
    
    for (; y < boundsY; y++){
        long long x2 = alpha.GetD() * y * y + _n;
        if (isPerfectSquare(x2)){
            long long x = std::sqrt(x2);
            if (nod(x, y) == 1)
                return {x, y};
        }
    }
    return {};
}

std::pair<long long, long long> PellsEquations::jSolNonForm(int j){
    std::pair<long long, long long> fundSolNF = FundSolNonForm();
    std::pair<long long, long long> jSolutionPells = jSolutions(j);
    
    long long x1 = fundSolNF.first, y1 = fundSolNF.second;
    long long u = jSolutionPells.first, v = jSolutionPells.second;
    return {u * x1 + v * y1 * alpha.GetD(), u * y1 + v * x1};
}
