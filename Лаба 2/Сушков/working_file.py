import matplotlib.pyplot as plt
from random import choice
from itertools import product

m = 0  # число благоприятных исходов
n = 90  # число всевозможных исходов

# список чисел от 1 до 90
all_list = [i for i in range(1, 91)]

for i in all_list:
    """
    Идем в цикле по числам от 1 до 90
    и если число нечетное, то прибавляем
    к переменной m единицу
    """
    if i % 2:
        m += 1

theoretic_prob = m / n  # высчитываем теоретическую вероятность

x = range(50, 50000, 50)  # диапазон от 50 до 50000 с шагом 50

# список куда будут добавляться значения абсолютного отклонения
abs_error = []

# список куда будут добавляться значения квадратичного отклонения
sq_error = []

for exp_num in x:
    y_i = 0  # переменная к которой добавляем благоприятные исходы
    for _ in range(exp_num):
        kegs = [choice(all_list) for i in range(2)]
        if kegs[0] % 2 and kegs[1] % 2:
            # если два выбранных числа нечетные, то увеличиваем
            # переменную y_i на единицу
            y_i += 1
    freq = y_i / exp_num  # находим частоту

    # находим абсолютное отклонение и добавляем в список
    abs_error.append(abs(theoretic_prob - freq))

    # находим квадратичное отклонение и добавляем в список
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
