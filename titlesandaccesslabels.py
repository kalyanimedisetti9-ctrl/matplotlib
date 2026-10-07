import matplotlib.pyplot as plt

Months = ["Jan", "Feb", "March", "Apr", "May"]
Revenue = [10000, 15000, 30000, 20000, 12000]

plt.plot(Months, Revenue, marker="o")

plt.title("Months & Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue")

plt.grid(True)

plt.show()