import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, linestyle="--", marker="o", color="r")

plt.title("Sales Performance")
plt.xlabel("Year")
plt.ylabel("Performance Score")

plt.grid(True)
plt.show()