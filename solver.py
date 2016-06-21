import re


class NotLinearEquationError(Exception):
    def __init__(self):
        super(NotLinearEquationError, self).__init__(
            "Your expression doesn't look like linear equation")


def solve(equation):
    if re.search(r"x[\*/]([\d\.]+[\*/])*x", equation):
        raise NotLinearEquationError()
    expression = equation.replace("=", "-(") + ")"
    try:
        c = eval(expression, {"x": 1j})
    except (SyntaxError, TypeError, NameError):
        raise NotLinearEquationError()
    if not c.imag:
        raise NotLinearEquationError()
    return -c.real/c.imag
