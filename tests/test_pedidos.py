import pytest

from app.pedidos import calcular_total


def test_calcular_total_pedido():
    productos = [
        {
            "nombre": "Hamburguesa",
            "precio": 18000,
            "cantidad": 2,
        },
        {
            "nombre": "Limonada",
            "precio": 6000,
            "cantidad": 1,
        },
    ]

    total = calcular_total(productos)

    assert total == 42000


def test_pedido_vacio():
    assert calcular_total([]) == 0


def test_cantidad_invalida():
    productos = [
        {
            "nombre": "Hamburguesa",
            "precio": 18000,
            "cantidad": 0,
        }
    ]

    with pytest.raises(
        ValueError,
        match="La cantidad debe ser mayor que cero",
    ):
        calcular_total(productos)
