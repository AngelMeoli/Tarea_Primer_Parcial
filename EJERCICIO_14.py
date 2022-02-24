"""Programa que recibe un número entero positivo, correspondiente al año de nacimiento y debe de mostrar si el 
año fue bisiesto o no. Almacenar el resultado y opción de mostrar historial."""


menu=int(input("----BIENVENDO SELECCIONE UNA OPCION---- \n 1- Nuevo registro \n 2- Ver datos \n 3- Salir \n"))


def ingreso():
    dato=int(input("Ingrese el año de nacimiento: "))

    if dato%4==0:
        resultado="Bisiesto"
        print(resultado)

    else:
        resultado="No Bisiesto"
        print(resultado)  

    archivo=open("EJERCICIO_14.txt","a")
    archivo.write("Año: ")
    archivo.write(str(dato))
    archivo.write(" Resultado: ")
    archivo.write(str(resultado))
    archivo.write("\n")
    archivo.close()

def lectura():
    print("Mostrar Historial \n")
    archivo=open("EJERCICIO_14.txt")
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

