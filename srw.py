import numpy as np
import matplotlib.pyplot as plt

class Quadratic_Irrationals:
    def __init__(self, p, Q, D):
        self.p = p
        self.Q = Q
        self.D = D
        self.res_q = []
        
    def period(self) -> int:
        pi, Qi = self.p, self.Q
        qi = int((pi + np.sqrt(self.D)) // Qi)

        seen = {}
        i = 0
        while (pi, Qi) not in seen:
            seen[(pi, Qi)] = i
            pi = qi * Qi - pi
            Qi = (self.D - pi * pi) // Qi
            qi = (pi + np.sqrt(self.D)) // Qi

            i+=1

        return i - seen[(pi, Qi)]

    def periodic_continued_fraction(self, number : int = 10) -> np.array:
        pi, Qi = self.p, self.Q
        qi = (pi + np.sqrt(self.D)) // Qi

        res_q = []
        
        for i in range(number):
            res_q.append(qi)
            pi = qi * Qi - pi
            Qi = (self.D - pi * pi) // Qi
            qi = (pi + np.sqrt(self.D)) // Qi
    

        return res_q

    @staticmethod
    def averaging(array: np.array) -> np.array:
        size = array.size
        result = [0]
        for D in range(2, size+1):  
            numerator = np.nansum(array[1:D])  
            denominator = D - np.sqrt(D)
            result.append(numerator / denominator)
        return np.array(result)


class PellsEquations:
    def __init__(self, D : Quadratic_Irrationals):
        self.D = D
        
    def fundamentalSolution(self) -> tuple:
        l = self.D.period()

        a_2, a_1 = 0, 1
        b_2, b_1 = 1, 0

        if(l % 2 ==0):
            pcf = self.D.periodic_continued_fraction(l)
            
        else:
            pcf = self.D.periodic_continued_fraction(2*l)
            

        for q in pcf:
            a_1_copy = a_1
            b_1_copy = b_1

            a_1 = q * a_1 + a_2
            a_2 = a_1_copy

            b_1 = q * b_1 + b_2
            b_2 = b_1_copy

        return a_1, b_1

    def jSolution(self, j : int) -> tuple:
        a,b = self.fundamentalSolution()

        x = (np.pow((a + b * np.sqrt(self.D.D)), j) + np.pow(a - b * np.sqrt(self.D.D), j)) / 2
        y = (np.pow(a + b * np.sqrt(self.D.D), j) -  np.pow(a - b * np.sqrt(self.D.D), j)) / 2

        return x, y



def main():
    k = Quadratic_Irrationals(0, 1, 425)
    
    equation = PellsEquations(k)
    print(equation.fundamentalSolution()) 
    print(equation.jSolution(3))



if __name__ == '__main__':
    main()