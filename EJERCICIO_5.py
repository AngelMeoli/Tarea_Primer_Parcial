"""Programa que muestra los numeros impares desde el 1 hasta el 100 e indica cuantos
numeros impares hay. Almacena el resultado y opcion de mostrar historial"""

menu =int(input("----BIENVENIDO SELECCIONE UNA OPCION---- \n 1- Calcular numeros impares \n 2- Ver historial \n 3- Salir \n"))

def ingreso():
    numero=int(input("Ingrese el numero: "))
    contador=0
    for c in range(numero+1):
        if c%2==1:
            contador=contador+1

    archivo=open("EJERCICIO_5.txt","a")
    archivo.write("Minimo:0 Maximo:")
    archivo.write(str(numero))
    archivo.write(" Numeros Impares:")
    archivo.write(str(contador))
    archivo.write("\n")
    archivo.close()

    print("Entre 0 y ",str(numero)," hay ",str(contador)," numeros impares")

def lectura():
    print("Mostrar Historial \n")
    archivo=open("EJERCICIO_5.txt")
    print(archivo.read())
    archivo.close()

while menu !=3:
    if menu ==1:
        ingreso()
    elif menu==2:
        lectura()
    else:
        print("Opcion no valida!")

    menu =int(input("----BIENVENIDO SELECCIONE UNA OPCION---- \n 1- Calcular numeros impares \n 2- Ver historial \n 3- Salir \n"))



