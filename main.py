import numpy as np
import matplotlib.pyplot as plt
from input import *
from methods.trapezoid import calculate_trapezoid
from methods.rectangles import calculate_rectangles
from methods.simpson import calculate_simpson

equation = choose_equation()
start, stop = choose_interval()
epsilon = choose_accuracy()

match choose_method():
    case 1:
        calculate_trapezoid(equation, start, stop, epsilon)
    case 2:
        calculate_rectangles(equation, start, stop, epsilon)
    case 3:
        calculate_simpson(equation, start, stop, epsilon)
    case _:
        print("Метода под таким номером нет!")

plt.plot([i for i in np.arange(start, stop, epsilon / 2)], [equation(i) for i in np.arange(start, stop, epsilon / 2)])
plt.title(f"[{start},{stop}]")
plt.show()
