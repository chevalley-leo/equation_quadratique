import pytest
from quadratic.solver import QuadraticEquation

def test_deux_solutions_reelles():
    eq = QuadraticEquation(1, -3, 2)
    x1, x2 = eq.solve()
    assert round(x1.real, 2) == 2.0
    assert round(x2.real, 2) == 1.0

def test_une_solution():
    eq = QuadraticEquation(1, 2, 1)
    x1, x2 = eq.solve()
    assert x1 == x2

def test_equation_non_valide():
    with pytest.raises(ValueError):
        QuadraticEquation(0, 1, 1)
