import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/results.csv")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))


# ax1.plot(df["nps_number"], df["period"], marker="o", linestyle="", alpha=0.6, color ="red" ,label="Период (неправильный)")
ax1.scatter(df["nps_number"], df["period_right"], marker="o", s=1, linestyle="", alpha=0.3, color="blue", label="Периоды")
ax1.set_xlabel("D (неполные квадраты)")
ax1.set_ylabel("Длина периода")
ax1.set_title("Зависимость периода от D")   
ax1.legend()
ax1.grid(True)


ax2.plot(range(len(df["avg_period"])), df["avg_period"], color="red", label="Средние периоды")
ax2.set_xlabel("D (неполные квадраты)")
ax2.set_ylabel("Средний период")
ax2.set_title("Усреднённые периоды")
ax2.legend()
ax2.grid(True)

plt.show()
