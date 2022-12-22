
import sympy
from sympy import simplify

# Решение примеров


def execute_expr(expr):
    expr1 = str(eval(expr))
    return expr1

# Решение уравнений


def solve_eq(expr):
    try:
        x = sympy.Symbol('x')
        result = str(sympy.solve(expr, x))
        return result
    except ValueError:
        print('Некорректный ввод')


# Упрощение многочленов

def simple(expr):
    return str(simplify(expr))
