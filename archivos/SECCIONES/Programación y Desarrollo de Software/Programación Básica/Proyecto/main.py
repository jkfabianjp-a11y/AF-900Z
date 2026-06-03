import funcionestrabajo
from productos import productos

sesiones = []

admin = "admin"
clave = "1234"

usuario = input("Ingrese el usuario: ")
contraseña = input("Ingrese la contraseña: ")

if usuario != admin or contraseña != clave:
    print("Usuario o contraseña incorrectos.")
    
if usuario == admin and contraseña == clave:
    print("Bienvenido al sistema de ventas.")
    while True:
        print("---- Cajero Abastecedor Rodriguez")
        print("-- Seleccione una de las opciones --")
        print("1. Cajero")
        print("2. Registro y visualización de cada venta")
        print("3. Módulo de informes")
        print("4. Salida del Sistema")
        print("")

        opcion_cajero = int(input("Ingrese una de las opciones mencionadas: "))

        if opcion_cajero == 1:
            ventas = []
            numero_venta = 1
            while True:
                producto = input("Ingrese el producto: ")
            
                item = None
                precio = 0

            # Buscar producto en toda la matriz
                for prod in productos:
                    if prod[0] == producto:
                        item = prod[0]
                        precio = prod[1]
                        break  # Detener búsqueda cuando se encuentra

                if item is not None:
                    cantidad = int(input("Ingrese la cantidad que desea llevar: "))
                    total = precio * cantidad
                    venta = funcionestrabajo.registrar_venta(numero_venta, item, precio, cantidad, total)
                    numero_venta += 1
                    ventas.append(venta)
                    print("")
                else:
                    print("Producto no válido.")
                    print("")

                salida_cajero = int(input("¿Desea salir del Sistema? (S = 1 /N = 2): "))
                if salida_cajero == 1:
                    if ventas:
                        sesiones.append(ventas)
                        print("")
                        break

        elif opcion_cajero == 2:
            if not sesiones:
                print("No hay ventas registradas.")
            else:
                indice_sesion = 0
                while indice_sesion < len(sesiones):
                    print("")
                    print("Sesión", indice_sesion + 1)
                    print("")
                    print("Resumen de la venta:")
                    ventas = sesiones[indice_sesion]
                    for venta in ventas:
                        funcionestrabajo.mostrarunaventa(venta)
                        print("")
                    total_sesion = 0
                    for v in ventas:
                        total_sesion += v[2] * v[3]
                    print("Total de la sesión: ₡" + str(total_sesion))
                    indice_sesion += 1

        elif opcion_cajero == 3:
            producto = input("Ingrese el producto para el informe: ")

            precio = None
            for prod in productos:
                if prod[0] == producto:
                    precio = prod[1]
                    break

            if precio is not None:
            # Unir todas las ventas de todas las sesiones
                todas_las_ventas = []
                for sesion in sesiones:
                    for venta in sesion:
                        todas_las_ventas.append(venta)
                funcionestrabajo.generar_informe(producto, todas_las_ventas, precio, 0)
                print("")
            else:
                print("Producto no válido.")
                print("")

        elif opcion_cajero == 4:
            print("Saliendo del sistema.")
            print("")
            break

        else:
            print("Opción no válida.")
            print("")
            break



