"""El Programa que recibe 3 números enteros positivos correspondiente a 3 notas, si el promedio es mayor o igual 
a 60 debe de mostrar un mensaje de aprobado, de lo contrario debe de mostrar un mensaje de reprobado, en ambos 
casos debe de mostrar el promedio. Almacenar el resultado y opción de mostrar historial."""

menu=int(input("----BIENVENDO SELECCIONE UNA OPCION---- \n 1- Nuevo registro \n 2- Ver datos \n 3- Salir \n"))

def ingreso():
    nota1=int(input("Ingrese la nota 1: "))
    nota2=int(input("Ingrese la nota 2: "))
    nota3=int(input("Ingrese la nota 3: "))


    promedio=(nota1+nota2+nota3)/3

    if promedio>=60:
        resultado="Aprobado"
        print("Promedio:",str(promedio)," Aprobado")

    elif promedio<60:
        resultado="Reprobado"
        print("Promedio:",str(promedio)," Reprobado")

    archivo=open("EJERCICIO_13.txt","a")
    archivo.write("Nota1: ")
    archivo.write(str(nota1))
    archivo.write(" Nota2: ")
    archivo.write(str(nota2))
    archivo.write(" Nota3: ")
    archivo.write(str(nota3))
    archivo.write(" Resultado: ")
    archivo.write(resultado)
    archivo.write("\n")
    archivo.close()   

def lectura():
    print("Mostrar Historial \n")
    archivo=open("EJERCICIO_13.txt")
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
