import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('data/results.csv')

    index = df['is_prime'] == 1

    prime_num = df.loc[index]['nps_number']
    period = df.loc[index]['period_right']


    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    ax1.scatter(prime_num, period, marker="o", s=5, linestyle="", alpha=0.3, color="blue", label="Периоды")
    ax1.set_xlabel('D (простые)')
    ax1.set_ylabel('Длины периодов')
    ax1.set_title('Зависимость периода от D простого')
    ax1.grid(True)

    val_counts = period.value_counts()
    ax2.scatter(val_counts.index, val_counts.values, marker='o', s=5,color='blue')
    ax2.set_xlabel('Длины периодов простых D')
    ax2.set_ylabel('Количество')
    ax2.set_title('Распределение длин периодов простых D')
    ax2.grid(True)
    
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()