import math

def choose_equation():
    print("Выберите уравнение:")
    print("1) cos(x)")
    print("2) x^3 +  2*x^2 - x")
    print("3) x^2 - x")

    match int(input()):
        case 1:
            equation = lambda x: math.cos(x)
        case 2:
            equation = lambda x: x ** 3 + 2 * x ** 2 - x
        case 3:
            equation = lambda x: x ** 2 - x
    return equation


def choose_interval():
    print("Введите начало интервала")
    start = float(input())
    print("Введите конец интервала")
    stop = float(input())
    return start, stop


def choose_accuracy():
    print("Введите точность:")
    return float(input())


def choose_method():
    print("Выберите метод:")
    print("1) Метод трапеций")
    print("2) Метод прямоугольников")
    print("3) Метод Симпсона")
    return int(input())
