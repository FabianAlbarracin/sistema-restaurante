def calcular_total(productos):
    """Calcula el total de un pedido.

    Cada producto debe incluir el precio y la cantidad solicitada.
    """
    if not productos:
        return 0

    total = 0

    for producto in productos:
        precio = producto["precio"]
        cantidad = producto["cantidad"]

        if precio < 0:
            raise ValueError("El precio no puede ser negativo")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        total += precio * cantidad

    return total
