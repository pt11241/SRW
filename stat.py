import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import make_interp_spline


def main():
    df = pd.read_csv('data/results.csv')

    counts = (df['period_right'].value_counts())

    arr, arr1, arr2, arr3, = [], [], [], []
    d = {0: arr, 1: arr1, 2: arr2, 3: arr3}
    
    for i in counts.index:
        d[i % 4].append([counts[i], i])
    
    arr = np.array(arr, dtype=int)
    arr1 = np.array(arr1, dtype=int)
    arr2 = np.array(arr2, dtype=int)
    arr3 = np.array(arr3, dtype=int)


    plt.figure(figsize=(10,6))

    plt.title('Распределение длины периодов')
    plt.xlabel('Длина периода')
    plt.ylabel('Количество')
    plt.grid(True)

    plt.scatter(arr[:, 1], arr[:, 0], label="4k", s=10)
    plt.scatter(arr1[:, 1], arr1[:, 0], label="4k+1", s=10)
    plt.scatter(arr2[:, 1], arr2[:, 0], label="4k+2", s=10)
    plt.scatter(arr3[:, 1], arr3[:, 0], label="4k+3", s=10)

    # plt.xlim(left=-100)
    # plt.ylim(bottom=-100)

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()


#  def main():
#     sns.set_style("whitegrid") 
#     sns.set_palette("muted") 
#     df = pd.read_csv('data/results.csv') 
#     plt.figure(figsize=(10, 6)) 
#     sns.histplot(df['period_right'],
#                   bins = 20, kde=True, 
#                   # stat='density', 
#                   # kde_kws=dict(cut=3),
#                   # color="royalblue", 
#                   alpha=0.7 )
#     plt.xlabel("Длины периодов") 
#     plt.ylabel("Плотность")
#     plt.title("Распределение длин периодов", fontsize=14)
#     plt.xlim(left=0) # ось X начинается с 0 
#     plt.ylim(bottom=0) # ось Y начинается с 0 
#     sns.despine() 
#     plt.show()