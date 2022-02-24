"""Desarrolle un programa que clasifique y almacene la información de un grupo de taxis, indicando si se encuentra en 
óptimas condiciones o necesita mantenimiento si debe renovarse. Las condiciones son las siguientes si es modelo menor 
a 2007 y tiene más de 20,000 km recorridos debe renovarse. Si es modelo mayor a 2013 y tiene menos de 10000km está en 
óptimas condiciones, si no cumple ninguna de las anteriores condiciones debe de desplegar un mensaje que diga mecánico.
Almacenar el resultado y opción de mostrar historial.
"""
menu=int(input("----BIENVENDO SELECCIONE UNA OPCION---- \n 1- Nuevo registro \n 2- Ver datos \n 3- Salir \n"))

def ingreso():

    modelo=int(input("Ingrese el año del taxi: "))
    km=int(input("Ingrese kilometraje del taxi: "))

    if modelo <2007 and km>20000:
        status=" El taxi debe renovarse"
        print(status)

    elif modelo>2007 and modelo<2013 and km>20000:
        status=" El taxi necesita mantentenimiento"
        print(status)

    elif modelo>2013 and km<10000:
        status=" Taxin en buenas condiciones"
        print(status)

    else:
        status=" mecanico"
        print(status)

    archivo=open("EJERCICIO_8.txt","a")
    archivo.write("Año del taxi: ")
    archivo.write(str(modelo))
    archivo.write(" Kilometraje: ")
    archivo.write(str(km))
    archivo.write(str(status))
    archivo.write("\n")
    archivo.close()

def lectura():
    print("Mostrar Historial \n")
    archivo=open("EJERCICIO_8.txt")
    print(archivo.read())
    archivo.close()

while menu!=3:
    if menu==1:
        ingreso()
    elif menu==2:
        lectura()

    else:
        print("Opcion Invalida!!")

    menu=int(input("----BIENVENDO SELECCIONE UNA OPCION---- \n 1- Nuevo registro \n 2- Ver datos \n 3- Salir \n"))
