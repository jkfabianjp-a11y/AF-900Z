import funciones

# Listas precargadas
numeros_venta = [1, 2, 3, 4]
clientes = ["Ana", "Luis", "María", "Pedro"]
frutas = ["Manzana", "Sandía", "Aguacate", "Manzana"]
kgs = [2, 5, 1.5, 3]
precios_frutas = [3, 1.5, 5, 3] 


while True:
    print("1. Registrar venta")
    print("2. Mostrar ventas")
    print("3. Reporte totales")
    print("4. Venta mayor")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        funciones.registrar_venta(numeros_venta, clientes, frutas, kgs, precios_frutas)
    elif opcion == "2":
        funciones.mostrar_ventas(numeros_venta, clientes, frutas, kgs, precios_frutas)
    elif opcion == "3":
        funciones.reporte_totales(frutas, kgs, precios_frutas)
    elif opcion == "4":
        funciones.venta_mayor(numeros_venta, clientes, frutas, kgs)
    elif opcion == "5":
        print("Saliendo...")
    else:
        print("Opción inválida.")




