from gmpy2 import mpz, mpq, mpfr, isqrt, sqrt
import math
import numpy as np

class Quadratic_Irrationals:
    def __init__(self, p, Q, D):
        self.p = mpz(p)
        self.Q = mpz(Q)
        self.D = mpz(D)

        
    def period(self) -> int:
        pi, Qi = self.p, self.Q

        qi = (pi + isqrt(self.D)) // Qi

        seen = {}
        i = 0
        while (pi, Qi) not in seen:
            seen[(pi, Qi)] = i
            pi = qi * Qi - pi
            Qi = (self.D - pi * pi) // Qi
            qi = (pi + isqrt(self.D)) // Qi
            i += 1

        return i - seen[(pi, Qi)]

    def periodic_continued_fraction(self, number: int = 10):
        pi, Qi = self.p, self.Q
        qi = (pi + isqrt(self.D)) // Qi

        res_q = []
        
        for i in range(number):
            res_q.append(qi)
            pi = qi * Qi - pi
            Qi = (self.D - pi * pi) // Qi
            qi = (pi + isqrt(self.D)) // Qi
    
        return res_q

    @staticmethod
    def averaging(array: np.array) -> np.array:
        size = array.size
        result = []
        for D in range(1, size+1):  
            numerator = np.nansum(array[1:D])  
            denominator = D - np.sqrt(D)
            result.append(numerator / denominator)
        return np.array(result)


class PellsEquations:
    def __init__(self, D: Quadratic_Irrationals):
        self.D = D
        self._fundamental_solution = None 
        
    def fundamentalSolution(self) -> tuple:

        if self._fundamental_solution is not None:
            return self._fundamental_solution
            
        l = self.D.period()

        a_2, a_1 = mpz(0), mpz(1)
        b_2, b_1 = mpz(1), mpz(0)

        if l % 2 == 0:
            pcf = self.D.periodic_continued_fraction(l)
        else:
            pcf = self.D.periodic_continued_fraction(2 * l)

        for q in pcf:
            a_1, a_2 = q * a_1 + a_2, a_1
            b_1, b_2 = q * b_1 + b_2, b_1

        self._fundamental_solution = (a_1, b_1)
        return self._fundamental_solution

    def jSolution(self, j: int) -> tuple:
        a, b = self.fundamentalSolution()
        D_val = self.D.D
        

        base = a + b * sqrt(mpfr(D_val))
        base_conj = a - b * sqrt(mpfr(D_val))
        

        x = (pow(base, j) + pow(base_conj, j)) / 2
        y = (pow(base, j) - pow(base_conj, j)) / (2 * sqrt(mpfr(D_val)))
        
        return x, y




def main():
    k = Quadratic_Irrationals(0, 1, 425)
    
    equation = PellsEquations(k)
    print(equation.fundamentalSolution())
    print(equation.jSolution(3))



if __name__ == '__main__':
    main()