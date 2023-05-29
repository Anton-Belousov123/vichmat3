def runge_rule_check(result_formula, a, b, e):
    num_of_intervals = 4
    h = calc_h(a, b, num_of_intervals)
    result = result_formula(h)
    prev_result = result + 1
    while abs(result - prev_result) > e:
        print(f"n = {num_of_intervals}      -      res = {result}")
        num_of_intervals *= 2
        h = calc_h(a, b, num_of_intervals)
        prev_result = result
        result = result_formula(h)
    return result, num_of_intervals


def calc_h(a, b, num_of_intervals):
    return abs(b - a) / num_of_intervals



