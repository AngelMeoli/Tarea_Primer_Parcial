"""Progrma que recibe tres numeros enteros positivo, que corresponde a los tres lados del triangulo
debe de mostrar si es Equilatero, Isoceles o Escaleno. Almacenar el resultado y opcion de mostrar el historial"""

menu=int(input("----BIENVENDO SELECCIONE UNA OPCION---- \n 1- Nuevo registro \n 2- Ver datos \n 3- Salir \n"))



def ingreso():
    lado1=int(input("Longitud 1: "))
    lado2=int(input("Longitud 2: "))
    lado3=int(input("Longitud 3: "))

    tipo=""
    if lado1==lado2==lado3:
        tipo="Equilatero"
        print("Triangulo Equilatero")

    elif ((lado1==lado2 or lado1==lado3 or lado2==lado3) and (lado1!=lado2 or lado1!=lado3 or lado2!=lado3)):
        tipo="Isoseles"
        print("Triagulo Isoseles")

    else:
        tipo="Escaleno"
        print("Triangulo Escaleno")

    archivo=open("EJERCICIO_6.txt","a")
    archivo.write(str(lado1))
    archivo.write(",")
    archivo.write(str(lado2))
    archivo.write(",")
    archivo.write(str(lado3))
    archivo.write(",")
    archivo.write(tipo)
    archivo.write("\n")
    archivo.close()

def lectura():
    print("Mostrar Historial \n")
    print("L1,L2,L3,TIPO ")
    archivo=open("EJERCICIO_6.txt")
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


    