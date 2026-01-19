def descuento(precio, porcentaje):
    if precio > 0:
        precio = precio * (1 - porcentaje / 100)
    return precio

def aplicarIVA(precio):
    if precio > 0:
        precio = precio * 1.21
    return precio

def aplicar_a_la_cesta(cesta, descuento):
    total = 0.0
    for precio, porcentaje in cesta.items():
        precio_final = descuento(precio, porcentaje)
        total += precio_final
    return total

cesta = {
    'pan': (0.80, 0),
    'leche': (1.50, 10),
    'manzanas': (2.00, 21)
}
