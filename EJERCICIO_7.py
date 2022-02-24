"""Desarrolle un programa que calcule el factorial de un  número si y sólo si este es divisible entre 
el número 7. Si no es divisible debe de mostrar un mensaje informando el error. 
Almacenar el resultado y opción de mostrar historial."""
menu=int(input("----BIENVENDO SELECCIONE UNA OPCION---- \n 1- Nuevo registro \n 2- Ver datos \n 3- Salir \n"))

def ingreso():
    nuemero=int(input("Ingrese un numero: "))
    
    if nuemero%7==0:
        b=1
        for c in range(nuemero+1):
        
            if c>0:
                b=b*c

        print("El factorial es: ",str(b))
        archivo=open("EJERCICIO_7.txt","a")
        archivo.write("Numero Igresado: ")
        archivo.write(str(nuemero))
        archivo.write(" Factorial: ")
        archivo.write(str(b))
        archivo.write("\n")
        archivo.close()
    else:
        print("El numero no es divisible dentro de 7")
        archivo=open("EJERCICIO_7.txt","a")
        archivo.write("Numero Igresado: ")
        archivo.write(str(nuemero))
        archivo.write(" Numero no valido ")
        archivo.write("\n")
        archivo.close()



def lectura():
    print("Mostrar Historial \n")
    archivo=open("EJERCICIO_7.txt")
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



