from calculadora import sumar


def test_suma_positivos():
    assert sumar(2, 5) == 7


def test_suma_con_cero():
    assert sumar(7, 0) == 7


def test_suma_negativos():
    assert sumar(-2, -3) == -5


def test_suma_decimales():
    assert sumar(1.5, 2.5) == 4.0
