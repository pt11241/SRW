#include "../include/QuadraticIrrationals.hpp"
#include <iostream>
#include <vector>
#include <cstddef> 
#include <fstream>
#include <chrono>
#include <gmpxx.h>
 



int main(){
    const auto start{std::chrono::steady_clock::now()};
    int p = 0, Q = 1;
    size_t max_D = 10000000;

    std::vector<long long> nps_numbers;
    std::vector<mpz_class> periods_right;
    std::vector<mpq_class> avg_periods2(1,0);

    QuadraticIrrationals::periods_and_averaging(nps_numbers, periods_right, avg_periods2, max_D, p, Q);

    std::ofstream fout("/home/brb484/projects/SRW/data/results.csv");  
    fout << "nps_number,period_right,avg_period\n";


    for (size_t i = 0; i < nps_numbers.size(); i++) {
        fout << nps_numbers[i] << "," 
             << periods_right[i] << ","
             << avg_periods2[i].get_d() << "\n";
    }

    fout.close();    

    const auto finish{std::chrono::steady_clock::now()};
    const std::chrono::duration<double> elapsed_seconds{finish - start};

    std::cout << elapsed_seconds.count() << '\n';

    return 0;
}