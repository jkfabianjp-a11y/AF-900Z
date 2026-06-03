def registrar_venta(numeros_venta, clientes, destino,tickets,precio_destino):#Registrar

    cliente = input("Indique el nombre del cliente: ")

    print()
    print("Indique el tipo de ticket que compro: ")
    print()
    print("1. Nacional")
    print("2. Internacional")
    print("3. VIP")
    print()
    op = input("Opción: ")

    if op == "1" or "Nacional" or "nacional":
        tile = "Nacional"
        precio = precio_destino [0]
    elif op == "2" or "Internacional" or "internacional":
        tile = "Internacional"
        precio = precio_destino[1]
    elif op == "3" or "VIP" or "vip":
        tile = "VIP"
        precio = precio_destino[2]
    else:
        print("Opción inválida.")
        return
    
    print()
    cantidad_tickets = int(input("Indique la cantidad de tickets que compro: "))
    print()

    num = len(numeros_venta) + 1
    numeros_venta.append(num)
    clientes.append(cliente)
    destino.append(tile)
    tickets.append(cantidad_tickets)
    precio_destino.append(precio)
    print()
    print("--------------------Venta registrada--------------------")
    print()

def mostrar_ventas(numeros_venta, clientes, destino, tickets, precio_destino):
    print()
    print("---------------------------------------------------------")
    for i in range(len(numeros_venta)):
        precio_total = tickets[i] * precio_destino[i]
        print(str(numeros_venta[i]) + " - " + clientes[i] + " - " + destino[i] + " - " + str(tickets[i]) + " tickets - $" + str(precio_total))
        print("---------------------------------------------------------")
    print()

def reporte_totales(destino, tickets, precio_destino):#Reporte
    print()
    print("---------------------------------------------------------")
    tickets_unicas = ["Nacional", "Internacional", "VIP"]
    precios_fijos = [400, 250, 600, 500]
    for j in range(len(tickets_unicas)):
        total_tickets = 0
        for i in range(len(destino)):
            if destino[i] == tickets_unicas[j]:
                total_tickets += tickets[i]
        total_precio = total_tickets * precios_fijos[j]
        print(tickets_unicas[j] + ": " + str(total_tickets) + " tickets - Total: $" + str(total_precio))
        print("---------------------------------------------------------")
    

def venta_mayor(numeros_venta, clientes, destino,tickets):#Venta Mayor
    print()
    print("---------------------------------------------------------")
    if len(tickets) == 0:
        print("No hay ventas.")
        return
    mayor_tickets = tickets[0]
    pos_mayor = 0
    for i in range(1, len(tickets)):
        if tickets[i] > mayor_tickets:
            mayor_tickets = tickets[i]
            pos_mayor = i
    print("Venta mayor: " + str(numeros_venta[pos_mayor]) + " - " + clientes[pos_mayor] + " - " + destino[pos_mayor] + " - " + str(tickets[pos_mayor]) + " tickets")
    print("---------------------------------------------------------")