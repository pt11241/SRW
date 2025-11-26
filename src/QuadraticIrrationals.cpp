#include "../include/QuadraticIrrationals.hpp"
#include <unordered_map>

struct PairHash {
    std::size_t operator()(const std::pair<long long, long long>& p) const noexcept {
        
        auto h1 = std::hash<long long>{}(p.first);
        auto h2 = std::hash<long long>{}(p.second);

        
        return h1 ^ (h2 << 1);
    }
};

bool isPerfectSquare(long long n) {
    if (n < 0) return false; 
    long long root = static_cast<long long>(std::sqrt(n));
    return root * root == n;
}

QuadraticIrrationals::QuadraticIrrationals(long long p_, long long Q_, long long D_)
        : p(p_), Q(Q_), D(D_) {}


int QuadraticIrrationals::period_right() {
    long long pi = p;
    long long Qi = Q;
    long long Dcopy = D;
    if ((D - p*p) % Q != 0){
        pi *= Q;
        Qi *= Q;
        Dcopy *= Q*Q;
    }
    double sqr = std::sqrt(D);
    long long sqrtD = isqrt(Dcopy);
    long long i = 0;
    long long qi = (pi + sqrtD) / Qi;
    if (((p + sqr) / Q) > 1 && ((p - sqr) / Q) < 0  && ((p - sqr) / Q) > -1){
        long long q0 = qi;
        pi = qi * Qi - pi;
        Qi = (Dcopy - pi * pi) / Qi;
        qi = (pi + sqrtD) / Qi;
        i++;
        while(q0 != qi){
            pi = qi * Qi - pi;
            Qi = (Dcopy - pi * pi) / Qi;
            qi = (pi + sqrtD) / Qi;
            i++;
        }
        return i;
    }else{
        std::unordered_map<std::pair<long long,long long>, long long, PairHash> seen; 
        while (seen.find({pi, Qi}) == seen.end()) {
            seen[{pi, Qi}] = i;
            pi = qi * Qi - pi;
            Qi = (Dcopy - pi * pi) / Qi;
            qi = (pi + sqrtD) / Qi;
            i++;
        }
        return i - seen[{pi, Qi}];
    }
}


mpz_class QuadraticIrrationals::periodD(){ // здесь всегда будет выполняться условие Q | D - P^2
    if(!(p == 0 && Q == 1))
        throw "p must be 0, Q must be 1 ";
    long long pi = p;
    long long Qi = Q;
    long long sqrtD = isqrt(D);
    mpz_class i = 1;
    long long qi = (pi + sqrtD) / Qi;
    long long q0 = qi;
    pi = qi * Qi - pi;
    Qi = (D - pi * pi) / Qi;
    qi = (pi + sqrtD) / Qi;
    while (qi != 2*q0){
        pi = qi * Qi - pi;
        Qi = (D - pi * pi) / Qi;
        qi = (pi + sqrtD) / Qi;
        i++;
    }
    return i;
}


std::vector<long long> QuadraticIrrationals::periodic_continued_fraction(int number = 10) {
    long long pi = p;
    long long Qi = Q;
    long long Dcopy = D;
    if((D - p*p) % Q != 0){
        pi *= Q;
        Qi *= Q;
        Dcopy *= Q*Q;
    }
    long long sqrtD = isqrt(Dcopy);
    std::vector<long long> res_q;
    for (int i = 0; i < number; i++) {
        long long qi = (pi + sqrtD) / Qi;
        res_q.push_back(qi);
        pi = qi * Qi - pi;
        Qi = (Dcopy - pi * pi) / Qi;
    }
    return res_q;
}

std::vector<double> QuadraticIrrationals::averaging(const std::vector<long long>& array) {
    int size = static_cast<int>(array.size());
    long long total = 0;
    std::vector<double> result;
    result.push_back(0.0);
    for (int D = 2; D <= size; D++) {
        total = total + array[D-1];
        double denominator = D - std::sqrt(D);
        if (denominator == 0.0) {
            result.push_back(std::numeric_limits<double>::infinity());
        } else {
            result.push_back(static_cast<double>(total) / denominator);
        }
    }
    return result;
}

void QuadraticIrrationals::periods_and_averaging(std::vector<long long> &a, std::vector<mpz_class> &b,
                           std::vector<mpq_class> &c, 
                           size_t maxD, int p = 0, int Q = 1){
    mpz_class total = 0;

    for (size_t i = 2; i < maxD; i++){
        if (isPerfectSquare(i)) 
            continue;
        a.push_back(i);
        QuadraticIrrationals QIrrational(p, Q, i);
        mpz_class period_right = QIrrational.periodD();
        b.push_back(period_right);

        total += period_right;
        mpq_class denominator = i - std::sqrt(i);
        c.push_back(total / denominator);
    }
}
