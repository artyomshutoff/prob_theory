import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.cos(np.sqrt(x) - 1) * np.exp(np.sqrt(2 * x)) / np.sqrt(x)


x_min = 2  # Левая граница области
x_max = 5  # Правая граница области

# х - вектор 100 значений от x_min до x_max
x = np.linspace(x_min, x_max, 100)
y = f(x)  # вектор-функция от х

y_min = min(y)  # Нижняя граница области
y_max = max(y)  # Верхняя граница области

# Рисуем график
plt.plot(x, y)
plt.axhline(y_max, color="red", linestyle="--")
plt.axhline(y_min, color="red", linestyle="--")
plt.axvline(x_min, color="red", linestyle="--")
plt.axvline(x_max, color="red", linestyle="--")

plt.show()

# Количество точек в прямоугольной области, чтобы с вероятностью
# р = 0.9 результат имел точность не менее 0.01
N = 6806

# Вектор полученных значений в испытаниях
results = []

# Площадь области испытаний - красного прямоугольника
D_measure = (x_max - x_min) * (y_max - y_min)

for _ in range(10):
    # Генерируем случайные точки внутри области
    exp_x = np.random.uniform(x_min, x_max, N)
    exp_y = np.random.uniform(y_min, y_max, N)

    # Считаем количество точек, попавших под
    # или на график функции
    m = len(exp_y[exp_y <= f(exp_x)])

    results.append(round(D_measure * m / N, 4))


print(*results, end="\n\n")
print("Итоговое значение:", round(np.mean(results), 4))
