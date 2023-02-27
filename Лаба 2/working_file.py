# artyomshutoff

import matplotlib.pyplot as plt
import numpy as np
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
    pass
    # y_i = sum([choice(all_list)])
