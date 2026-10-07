import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [20, 35, 25, 40]

plt.plot(months, sales)

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()