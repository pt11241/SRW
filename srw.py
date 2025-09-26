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
    def med(array: np.array) -> np.array:
        size = array.size
        result = []
        for D in range(1, size+1):  
            numerator = np.nansum(array[1:D])  
            denominator = D - np.sqrt(D)
            result.append(numerator / denominator)
        return np.array(result)


def main():
    k = Quadratic_Irrationals(4, 6, 22)
    print(k.periodic_counted_fraction(20))
    p0,Q0 = 0, 1
    D = np.arange(1, 1000)
    indx = np.sqrt(D) % 1 != 0
    D = D[indx]
    lens = np.array([Quadratic_Irrationals(p0, Q0, i).period() for i in D])

    # x_D = Quadratic_Irrationals.med(D)
    Lmed = Quadratic_Irrationals.med(lens)
    print(lens[:10])
    print("AAAAAAAAAAAAAAa")
    print(Lmed[:10])

    
    plt.figure(figsize=(14, 7))

    DmedGraph = plt.plot(D, Lmed, color='b', alpha=1, label='Усреднённые значения', linewidth=3)
    lens_D = plt.plot(D, lens, 'o', color='g', alpha=0.3, label='Периоды')
    # plt.plot(D, Lmed, 'o-', color='b', alpha=0.8, label='Усреднённые значения')
    # plt.plot(D, lens, '-', color='g', alpha=0.6, label='Периоды')
    plt.legend()

    plt.title("Длины периодов и их усреднение")
    plt.grid()
    plt.xlabel("D")
    plt.ylabel("L(D)")
    plt.show()


if __name__ == '__main__':
    main()