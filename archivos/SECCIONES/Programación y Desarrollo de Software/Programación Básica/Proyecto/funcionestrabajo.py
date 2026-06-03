# Registrar una venta
def registrar_venta(numero_venta, producto, precio, cantidad, total):
    total = precio * cantidad
    print("---- Venta Registrada ----")
    print("Número de venta:", numero_venta)
    print("Producto:", producto)
    print("Precio unitario: ₡", precio)
    print("Cantidad:", cantidad)
    print("Total: ₡", total)
    print("")
    venta = (numero_venta, producto, precio, cantidad, total)
    return venta

# Mostrar una venta
def mostrarunaventa(venta):
    print("---- Detalle de la Venta ----")
    print("Número de venta:", venta[0])
    print("Producto:", venta[1])
    print("Precio unitario: ₡", venta[2])
    print("Cantidad:", venta[3])
    total = venta[2] * venta[3]
    print("Total: ₡" + str(total))
    print("")

# Generar informe
def generar_informe(producto, ventas, precio, cantidad):
    print("---- Informe ----")
    total_general = 0
    total_cantidad = 0
    for i in ventas:
        if i[1] == producto:
            total_general += i[2] * i[3]
            total_cantidad += i[3]
    print(producto + ": " + str(total_cantidad) + " unidades")
    print("Total generado: ₡" + str(total_general))
