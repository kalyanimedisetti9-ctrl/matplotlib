import matplotlib.pyplot as plt

ages = [18, 20, 22, 25, 25, 28, 30, 32, 35, 36,
        40, 42, 45, 48, 50, 52, 55, 58]

plt.hist(
    ages,
    bins=10,
    range=(18, 60)
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of People")

plt.show()