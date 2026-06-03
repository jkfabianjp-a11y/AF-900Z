
respuesta = "S"
cantClientesRecomienda = 0
cantClientesNoRecomienda = 0

while respuesta != "X":
    respuesta = input("Recomendaria el nuevo medicamneto natural? (S para si, N para no, X para salir): ")

    if respuesta == "S":
        print("Gracias por confiar en la medicina natural")
        cantClientesRecomienda += 1
    
    elif respuesta == "N":
        print("Gracias por su sinceridad, tomaremos en cuenta su opinion")
        cantClientesNoRecomienda += 1

    elif respuesta == "X":
        print("Cantidad de personas que si recomiendan el nuevo medicamento" , cantClientesRecomienda)
        print("Cantidad de personas que no recomiendan el nuevo medicamento" , cantClientesNoRecomienda)
    
    else:
        print("Las opciones validas son: (S para si, N para no, X para salir) ")