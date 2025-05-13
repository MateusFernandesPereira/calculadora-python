# test_calculator.py

import pytest
from calculator_core import evaluate_expression

@pytest.mark.parametrize("expression,expected", [
    ("1+1", "2"),
    ("2*3", "6"),
    ("10/2", "5.0"),
    ("5-3", "2"),
    ("2**3", "8"),
    ("9/0", "Erro"),
    ("10+", "Erro"),
    ("(3+2)*2", "10"),
    ("-5+3", "-2"),
    ("4.5*2", "9.0"),
    ("0.1+0.2", str(0.1+0.2)),  # cuidado com float
    ("2^3", "Erro"),
    ("3*()", "Erro"),
    ("abc", "Erro"),
    ("", "Erro"),
    ("100-50+25", "75"),
    ("10/3", str(10/3)),
    ("(2+2)*(2+2)", "16"),
    ("3.1415*2", str(3.1415*2)),
    ("3--3", "6"),
])
def test_evaluate_expression(expression, expected):
    assert evaluate_expression(expression) == expected
