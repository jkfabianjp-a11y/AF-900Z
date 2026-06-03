import funciones

print()
print("Bienvenido(a) al registro de agencia de viejes")
print()
print("Selecciones una de las opciones de la siguiente lista:")
print()

# Listas precargadas
numeros_venta = [1, 2, 3, 4]
clientes = ["Ana", "Gerardo", "Santiago", "Pedro"]
destino = ["Internacional","Nacional","VIP","Nacional"]
tiques = [3, 2, 1, 4]
precios_destino = [400, 250, 600, 250] 

while True:
    print("[1]. Registro de Tickets")
    print("[2]. Mostrar Todas las ventas")
    print("[3]. Reporte totales")
    print("[4]. Venta con mas Tickets")
    print("[5]. Salir")
    print()

    opcion = input("Opción: ")

    if opcion == "1":
        funciones.registrar_venta(numeros_venta,clientes,destino,tiques,precios_destino)
    elif opcion == "2":
        funciones.mostrar_ventas(numeros_venta,clientes,destino,tiques,precios_destino)
    elif opcion == "3":
        funciones.reporte_totales(destino,tiques,precios_destino)
    elif opcion == "4":
        funciones.venta_mayor(numeros_venta,clientes,destino,tiques)
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")








