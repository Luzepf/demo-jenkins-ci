import pytest
from calculadora import sumar, restar, multiplicar, dividir


def test_sumar():
    assert sumar(2, 3) == 5


def test_restar():
    assert restar(10, 4) == 6


def test_multiplicar():
    assert multiplicar(3, 4) == 12


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)
