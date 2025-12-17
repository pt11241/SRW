import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def prime4k13(dfPrimePeriods):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 10))

    p4k1 = dfPrimePeriods.loc[dfPrimePeriods['nps_number'] % 4 == 1]
    p4k3 = dfPrimePeriods.loc[dfPrimePeriods['nps_number'] % 4 == 3]
    valueCountP4K1 = p4k1['period_right'].value_counts()
    valueCountP4K3 = p4k3['period_right'].value_counts()

    ax1.scatter(p4k1['nps_number'], p4k1['period_right'], marker="o", alpha=0.7, s=0.05)
    ax1.grid(True)
    ax1.set_xlabel('D = 4k + 1, D - prime')
    ax1.set_ylabel('Длина периода')

    ax2.scatter(p4k3['nps_number'], p4k3['period_right'], marker="o", alpha=0.7, s=0.05)
    ax2.grid(True)
    ax2.set_xlabel('D = 4k + 3, D - prime')
    ax2.set_ylabel('Длина периода')

    ax3.scatter(valueCountP4K1.index, valueCountP4K1.values, s=5)
    ax3.grid(True)

    ax4.scatter(valueCountP4K3.index, valueCountP4K3.values, s=5)
    ax4.grid(True)

    plt.show()



def func(prime_num, period):

    fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, figsize=(14, 10))
    ax1.scatter(prime_num, period, marker="o", s=1, linestyle="", alpha=0.3, color="blue", label="Периоды")
    ax1.set_xlabel('D (простые)')
    ax1.set_ylabel('Длины периодов')
    ax1.set_title('Зависимость периода от D простого')
    ax1.grid(True)

    val_counts = period.value_counts()

    arr, arr1, arr2, arr3, = [], [], [], []
    d = {0: arr, 1: arr1, 2: arr2, 3: arr3}
    
    for i in val_counts.index:
        d[i % 4].append([val_counts[i], i])
    
    arr = np.array(arr, dtype=int)
    arr1 = np.array(arr1, dtype=int)
    arr2 = np.array(arr2, dtype=int)
    arr3 = np.array(arr3, dtype=int)

    ax2.scatter(arr[:, 1], arr[:, 0], label="4k", marker="o", s=10)
    ax2.scatter(arr1[:, 1], arr1[:, 0], label="4k+1",marker="o",  s=10)
    ax2.scatter(arr2[:, 1], arr2[:, 0], label="4k+2", marker="o", s=10)
    ax2.scatter(arr3[:, 1], arr3[:, 0], label="4k+3", marker="o", s=10)

    # ax2.scatter(val_counts.index, val_counts.values, marker='o', s=5,color='blue')
    ax2.set_xlabel('Длины периодов простых D')
    ax2.set_ylabel('Количество')
    ax2.set_title('Распределение длин периодов простых D')
    ax2.legend()
    ax2.grid(True)

    ax3.scatter(arr[:, 1], arr[:, 0], label="4k", marker="o", s=10)
    ax3.set_xlabel('Длины периодов простых D % 4 == 0')
    ax3.set_ylabel('Количество')
    ax3.set_title('Распределение длин периодов простых D')
    ax3.legend()
    ax3.grid(True)

    ax4.scatter(arr3[:, 1], arr3[:, 0], label="4k+3", marker="o", s=10)
    ax4.set_xlabel('Длины периодов простых D % 4 == 3')
    ax4.set_ylabel('Количество')
    ax4.set_title('Распределение длин периодов простых D')
    ax4.legend()
    ax4.grid(True)

    df2 = pd.DataFrame({'prime_num' : prime_num, 'period' : period})
    prime0 = df2.loc[(df2['period'] % 4) == 0]
    prime2 = df2.loc[((df2['period'] % 4) == 2)]
    prime1 = df2.loc[(df2['period'] % 4) == 1]
    prime3 = df2.loc[((df2['period'] % 4) == 3)]

    ax5.scatter(prime1['prime_num'], prime1['period'], marker="o", s=1, linestyle="", alpha=0.3, color="#02a32a", label="Периоды")
    ax5.set_xlabel('D (простые)')
    ax5.set_ylabel('Длины периодов % 4 == 1')
    ax5.set_title('Зависимость периода от D простого')
    ax5.grid(True)
    
    ax6.scatter(prime3['prime_num'], prime3['period'], marker="o", s=1, linestyle="", alpha=0.3, color="#02a32a", label="Периоды")
    ax6.set_xlabel('D (простые)')
    ax6.set_ylabel('Длины периодов % 4 == 3')
    ax6.set_title('Зависимость периода от D простого')
    ax6.grid(True)

    ax7.scatter(prime0['prime_num'], prime0['period'], marker="o", s=1, linestyle="", alpha=0.3, color="#02a32a", label="Периоды")
    ax7.set_xlabel('D (простые)')
    ax7.set_ylabel('Длины периодов % 4 == 0')
    ax7.set_title('Зависимость периода от D простого')
    ax7.grid(True)

    ax8.scatter(prime2['prime_num'], prime2['period'], marker="o", s=1, linestyle="", alpha=0.3, color="#02a32a", label="Периоды")
    ax8.set_xlabel('D (простые)')
    ax8.set_ylabel('Длины периодов % 4 == 2')
    ax8.set_title('Зависимость периода от D простого')
    ax8.grid(True)


    plt.legend()
    plt.show()

def func3(df, index):
    df = df[index]
    df2 = df.loc[df['nps_number'] % 4 == 3][['nps_number', 'period_right']]
    df3 = df.loc[df['period_right'] % 4 == 0][['nps_number', 'period_right']]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 10))

    vc1 = df2['period_right'].value_counts()
    vc2 = df3['period_right'].value_counts()

    ax1.scatter(vc1.index, vc1.values)
    ax2.scatter(vc2.index, vc2.values)

    plt.show()


def main():
    df = pd.read_csv('data/results.csv')

    index = df['is_prime'] == 1
    periodsnp = df['period_right'].copy()

    prime_num = df.loc[index]['nps_number']
    period = df.loc[index]['period_right']

    # fig, ax = plt.subplots(figsize=(14, 10))
    # ax.scatter(prime_num, period, marker="o", s=1, linestyle="", alpha=0.3, color="blue", label="Периоды")
    # ax.set_xlabel('D (простые)')
    # ax.set_ylabel('Длины периодов')
    # ax.set_title('Зависимость периода от D простого')
    # ax.grid(True)
    # plt.show()

    # print(periodsnp.median(), period.median())
    # print(periodsnp.mean(), period.mean())
    # func(prime_num, period)
    prime4k13(df.loc[index])
    # func3(df, index)

    # p43 = df2.loc[df2['nps_number'] % 4 == 3]
    # p43.loc[:,'is_l4'] = (p43['period_right'] % 4 == 2)


    # l4 = df2.loc[df2['period_right'] % 4 == 0]
    # l4['is_p43'] = (l4['nps_number'] % 4 == 3)
    # dolyap43_l4 = l4['is_p43'].sum()
    # dolyal4_p43 = p43['is_l4'].sum()

    # lengthl4 = len(l4)
    # lengthp43 = len(p43)
    
    # print(dolyal4_p43, dolyap43_l4)
    # print(lengthp43, lengthl4)

    # print(dolyal4_p43 / lengthp43)



if __name__ == '__main__':
    main()