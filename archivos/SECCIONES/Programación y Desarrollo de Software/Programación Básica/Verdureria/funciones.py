def registrar_venta(numeros_venta, clientes, frutas, kgs, precios_frutas):
    cliente = input("Nombre del cliente: ")

    print("1. Manzana")
    print("2. Sandía")
    print("3. Aguacate")
    op = input("Opción: ")

    if op == "1":
        fruta = "Manzana"
        precio = precios_frutas[0]
    elif op == "2":
        fruta = "Sandía"
        precio = precios_frutas[1]
    elif op == "3":
        fruta = "Aguacate"
        precio = precios_frutas[2]
    else:
        print("Opción inválida.")
        return

    kg = float(input("Cantidad en kg: "))

    num = len(numeros_venta) + 1
    numeros_venta.append(num)
    clientes.append(cliente)
    frutas.append(fruta)
    kgs.append(kg)
    precios_frutas.append(precio)
    print("Venta registrada.")

def mostrar_ventas(numeros_venta, clientes, frutas, kgs, precios_frutas):
    for i in range(len(numeros_venta)):
        precio_total = kgs[i] * precios_frutas[i]
        print(str(numeros_venta[i]) + " - " + clientes[i] + " - " + frutas[i] + " - " + str(kgs[i]) + " kg - ¢" + str(precio_total))

def reporte_totales(frutas, kgs, precios_frutas):
    frutas_unicas = ["Manzana", "Sandía", "Aguacate"]
    precios_fijos = [3, 1.5, 5]
    for j in range(len(frutas_unicas)):
        total_kg = 0
        for i in range(len(frutas)):
            if frutas[i] == frutas_unicas[j]:
                total_kg += kgs[i]
        total_precio = total_kg * precios_fijos[j]
        print(frutas_unicas[j] + ": " + str(total_kg) + " kg - Total: ¢" + str(total_precio))

def venta_mayor(numeros_venta, clientes, frutas, kgs):
    if len(kgs) == 0:
        print("No hay ventas.")
        return

    mayor_kg = kgs[0]
    pos_mayor = 0
    for i in range(1, len(kgs)):
        if kgs[i] > mayor_kg:
            mayor_kg = kgs[i]
            pos_mayor = i

    print("Venta mayor: " + str(numeros_venta[pos_mayor]) + " - " + clientes[pos_mayor] + " - " + frutas[pos_mayor] + " - " + str(kgs[pos_mayor]) + " kg")
