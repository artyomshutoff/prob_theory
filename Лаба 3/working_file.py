import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2**x * np.sin(x) * np.tan(x / 2)


x_min = -2
x_max = 0

x = np.linspace(x_min, x_max, 100)
y = f(x)

y_min = min(y)
y_max = max(y)

plt.plot(x, y)
plt.axhline(y_max, color="red", linestyle="--")
plt.axhline(y_min, color="red", linestyle="--")
plt.axvline(x_min, color="red", linestyle="--")
plt.axvline(x_max, color="red", linestyle="--")

plt.show()

N = 7000

results = []

D_measure = (x_max - x_min) * (y_max - y_min)

for _ in range(10):
    exp_x = np.random.uniform(x_min, x_max, N)
    exp_y = np.random.uniform(y_min, y_max, N)

    m = len(exp_y[exp_y <= f(exp_x)])

    results.append(round(D_measure * m / N, 4))

print(*results, end="\n\n")
print("Итоговое значение:", round(np.mean(results), 4))
