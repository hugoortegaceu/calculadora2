# tests/test_calculadora.py﻿
import pytest
from modulos_utiles.calculadora import Calculadora 
 
@pytest.fixture 
def test_suma():
    calc = Calculadora()
    assert calc.suma(2, 3) == 5
    assert calc.suma(-1, 1) == 0
 
def test_resta():
    calc = Calculadora()
    assert calc.resta(5, 3) == 2
    assert calc.resta(0, 5) == -5
 
def test_multiplicar():
    calc = Calculadora()
    assert calc.multiplicar(2, 3) == 6
    assert calc.multiplicar(-2, 3) == -6
 
def test_dividir():
    calc = Calculadora()
    assert calc.dividir(6, 3) == 2
    assert calc.dividir(5, 0) == "Error"  # Error intencional: no maneja correctamente la división por cero
