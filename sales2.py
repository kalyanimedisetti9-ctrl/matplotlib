import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [20, 35, 25, 40]
customers = [100, 150, 120, 180]

fig, ax1 = plt.subplots()

ax1.plot(months, sales, marker="o")
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales")

ax2 = ax1.twinx()
ax2.plot(months, customers, marker="o")
ax2.set_ylabel("Customers")

plt.title("Sales and Customers")
plt.show()