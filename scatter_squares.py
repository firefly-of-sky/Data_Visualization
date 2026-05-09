import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 设置图题并给坐标轴加上标签
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 5100, 0, 125_000_000_000])

# 设置刻度标记的样式
ax.tick_params(labelsize=14)

plt.show()
# plt.savefig("squares_plot.png", bbox_inches="tight")
