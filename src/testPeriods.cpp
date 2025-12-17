#include "../include/QuadraticIrrationals.hpp"
#include <iostream>
#include <vector>
#include <cstddef> 
#include <fstream>
#include <chrono>
#include <gmpxx.h>



int main(){
    int p = 0, Q = 1;
    size_t max_D = 1000000;
    std::cout << "Dmax = ";
    std::cin >> max_D; 
    bool flag = 1;
    const auto start{std::chrono::steady_clock::now()};
    

    std::vector<long long> nps_numbers;
    std::vector<mpz_class> periods_right2;
    std::vector<mpq_class> avg_periods2(1,0);

    std::vector<int> is_prime(max_D+1, 1);
    for (int i = 2; i <= max_D; i++){
        if (is_prime[i]){
            for (int j = 2 * i; j <= max_D; j += i){
                is_prime[j] = 0;
            }
        }  
    }

    // QuadraticIrrationals::periods_and_averaging(nps_numbers, periods_right2, avg_periods2, max_D, p, Q);
    size_t size = nps_numbers.size();
    std::vector<int> is_prime_nps(size);

    for (size_t i = 0; i < size; i++){
        if(is_prime[nps_numbers[i]]){
            is_prime_nps[i] = 1;
        }
        else{
            is_prime_nps[i] = 0;
        }
    }

    std::ofstream fout("/home/brb484/projects/SRW/data/results.csv");  
    fout << "nps_number,period_right,avg_period,is_prime\n";


    for (size_t i = 0; i < nps_numbers.size(); i++) {
        fout << nps_numbers[i] << "," 
             << periods_right2[i] << ","
             << avg_periods2[i].get_d() << ","
             << is_prime_nps[i] << "\n";
    }

    fout.close();    
    


    const auto finish{std::chrono::steady_clock::now()};
    const std::chrono::duration<double> elapsed_seconds{finish - start};

    std::cout << elapsed_seconds.count() << '\n';

    return 0;
}