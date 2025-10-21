from gmpy2 import mpz, mpq, mpfr, isqrt, sqrt
import math
import numpy as np
import matplotlib.pyplot as plt

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
    def averaging(array):
        size = array.size
        total = 0
        result = [0]
        for D in range(2, size+1):
            total += mpz(array[D-1])
            denominator = D - math.sqrt(D)
            result.append(total / denominator)
        
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
    # k = Quadratic_Irrationals(0, 1, 425)
    
    # equation = PellsEquations(k)
    # print(equation.fundamentalSolution())
    # print(equation.jSolution(3))
    p,Q = 0, 1

    D = np.arange(1, 10000000)
    indx = np.sqrt(D) % 1 != 0
    D = D[indx]
    lens = np.array([Quadratic_Irrationals(p, Q, i).period() for i in D])
    Lmed = Quadratic_Irrationals.averaging(lens)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ax1.plot(D, Lmed, color='b', alpha=1, label='Усреднённые значения', linewidth=3)
    ax1.set_title('Усреднённые значения L(D)')
    ax1.set_xlabel('D')
    ax1.set_ylabel('L(D)')
    ax1.grid()
    ax1.legend()

    ax2.plot(D, lens, 'o', color='g', alpha=0.5, label='Периоды')
    ax2.set_title('Длины периодов')
    ax2.set_xlabel('D')
    ax2.set_ylabel('L(D)')
    ax2.grid()
    ax2.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()