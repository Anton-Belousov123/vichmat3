import numpy as np
from calc_integral import runge_rule_check


def calculate_trapezoid(f, a, b, e):
    result_formula = lambda h: (sum([f(i) for i in np.arange(a + h, b, h)]) + (f(a) + f(b)) / 2) * h
    result, num_of_intervals = runge_rule_check(result_formula, a, b, e)
    print(f"Интеграл = {result}")
    print(f"Число интервалов = {num_of_intervals}")


