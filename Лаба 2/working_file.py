# artyomshutoff

import matplotlib.pyplot as plt
from random import choice
from itertools import product

m = 0
n = 0
all_list = []

for i in product(range(1, 7), repeat=2):
    if i[0] % 2 and i[1] % 2:
        m += 1
    n += 1
    all_list.append(list(i))

theoretic_prob = m / n

x = range(50, 50000, 50)
abs_error = []
sq_error = []

for exp_num in x:
    y_i = 0
    for _ in range(exp_num):
        dice = choice(all_list)
        if dice[0] % 2 and dice[1] % 2:
            y_i += 1
    freq = y_i / exp_num
    abs_error.append(abs(theoretic_prob - freq))
    sq_error.append((theoretic_prob - freq) ** 2)

fig, axes = plt.subplots(1, 2, figsize=(10, 6))

plt.subplots_adjust(wspace=0.3)
plt.suptitle(
    "Зависимость отклонения частоты события от его вероятности от количества испытаний"
)

axes[0].set_title("Абсолютное отклонение")
axes[0].plot(x, abs_error)
axes[1].set_title("Квадратичное отклонение")
axes[1].plot(x, sq_error)

plt.show()
