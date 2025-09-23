import numpy as np
import matplotlib.pyplot as plt

class Quadratic_Irrationals:
    def __init__(self, p, Q, D):
        self.p = p
        self.Q = Q
        self.D = D
        
    def period(self) -> int:
        pi, Qi = self.p, self.Q
        qi = int((pi + np.sqrt(self.D)) // Qi)

        res_q = []
        seen = set()

        while (pi, Qi) not in seen:
            res_q.append(qi)
            seen.add((pi, Qi))
            pi = qi * Qi - pi
            Qi = (self.D - pi * pi) // Qi
            qi = (pi + np.sqrt(self.D)) // Qi

        return len(res_q) - 1

    def periodic_counted_fraction(self, number : int) -> np.array:
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
    def med(array : np.array, step : int) -> np.array:
        part = len(array) // step
        return [np.mean(array[i * step: (i + 1) * step]) for i in range(part)]
   


def main():
    k = Quadratic_Irrationals(4, 6, 22)
    print(k.periodic_counted_fraction(20))
    p0,Q0 = 0, 1
    D = np.arange(1, 40000)
    indx = np.sqrt(D) % 1 != 0
    D = D[indx]
    lens = np.array([Quadratic_Irrationals(p0, Q0, i).period() for i in D])
    print(len(D))

    x_D = Quadratic_Irrationals.med(D, 500)
    Lmed = Quadratic_Irrationals.med(lens, 500)
    print(lens[:10])
    print("AAAAAAAAAAAAAAa")
    print(Lmed)

    
    DmedGraph = plt.plot(x_D, Lmed, color='b', alpha=1)
    lens_D = plt.plot(D, lens, color='g', alpha=0.7)

    # plt.setp(lens_D[0])
    plt.grid()
    plt.xlabel("D")
    plt.ylabel("L(D)")
    plt.show()


if __name__ == '__main__':
    main()