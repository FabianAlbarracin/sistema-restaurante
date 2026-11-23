class GestorReservas:
    def __init__(self):
        self.reservas = []

    def registrar_reserva(self, nombre, fecha, personas):
        if not nombre.strip():
            raise ValueError("El nombre es obligatorio")

        if not fecha.strip():
            raise ValueError("La fecha es obligatoria")

        if personas <= 0:
            raise ValueError("La cantidad de personas debe ser mayor que cero")

        reserva = {
            "nombre": nombre,
            "fecha": fecha,
            "personas": personas,
        }

        self.reservas.append(reserva)

        return reserva

    def consultar_reservas(self):
        return self.reservas
