import pytest

from app.reservas import GestorReservas


def test_registrar_y_consultar_reserva():
    gestor = GestorReservas()

    reserva = gestor.registrar_reserva(
        nombre="Laura Gómez",
        fecha="2026-11-28",
        personas=4,
    )

    reservas = gestor.consultar_reservas()

    assert reserva in reservas
    assert len(reservas) == 1
    assert reservas[0]["nombre"] == "Laura Gómez"
    assert reservas[0]["personas"] == 4


def test_reserva_con_personas_invalidas():
    gestor = GestorReservas()

    with pytest.raises(
        ValueError,
        match="La cantidad de personas debe ser mayor que cero",
    ):
        gestor.registrar_reserva(
            nombre="Carlos Pérez",
            fecha="2026-11-29",
            personas=0,
        )


def test_reserva_sin_nombre():
    gestor = GestorReservas()

    with pytest.raises(
        ValueError,
        match="El nombre es obligatorio",
    ):
        gestor.registrar_reserva(
            nombre="",
            fecha="2026-11-29",
            personas=2,
        )
