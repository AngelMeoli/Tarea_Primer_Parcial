"""Realizar una calculadora de areas geometricas de: circulo, triangulo, cuadrado, rectangulo.
                   Almacenar el resultado y la opcion de mostrar el historial"""


import numpy as np
import psycopg2

try:
    conexion=psycopg2.connect(
        host ="localhost",
        port = "5432",
        user = "postgres",
        password = "angel",
        dbname = "redes"
    )
    print("CONEXION EXITOSA")
except psycopg2.Error as e:
    print("HUBOUN ERROR EN LA CONEXION")

menu=int(input("----BIENVENDO SELECCIONE UNA OPCION---- \n 1- Circulo \n 2- Triangulo \n 3- Cuadrado \n 4- Rectangulo \n 5- Ver datos \n 6- Salir \n"))

def circulo():
    print("----Area del Circulo------")
    r=int(input("Ingrese el radio del circulo: "))
    area=round(np.pi*r**2, 2)
    print("-----El area es:", area,"------")

    figura="Circulo"
    cursor= conexion.cursor()
    cursor.execute("INSERT INTO areas (valor_1,area,figura) VALUES(%s,%s,%s);",(r,area,figura))
    conexion.commit()
    cursor.close()

    archivo=open("EJERCICIO_12.txt","a")
    archivo.write("Circulo ")
    archivo.write("Radio:")
    archivo.write(str(r))
    archivo.write(" Area: ")
    archivo.write(str(area))
    archivo.write("\n")
    archivo.close()


def triangulo():
    print("----Area del Triangulo------")
    b=int(input("Ingrese la base: "))
    h=int(input("Ingrese la altura: "))
    area=(b*h)/2
    print("-----El area es:", area,"------")

    archivo=open("EJERCICIO_12.txt","a")
    archivo.write("Triangulo ")
    archivo.write("Base:")
    archivo.write(str(b))
    archivo.write(" Altura:")
    archivo.write(str(h))
    archivo.write(" Area: ")
    archivo.write(str(area))
    archivo.write("\n")
    archivo.close()

def cuadrado():
    print("----Area del Cuadrado------")
    l=int(input("Ingrese la arista: "))
    area=l**2
    print("-----El area es:", area,"------")

    archivo=open("EJERCICIO_12.txt","a")
    archivo.write("Cuadrado ")
    archivo.write("Arista:")
    archivo.write(str(l))
    archivo.write(" Area: ")
    archivo.write(str(area))
    archivo.write("\n")
    archivo.close()

def rectangulo():
    print("----Area del Rectangulo------")
    b=int(input("Ingrese la base: "))
    h=int(input("Ingrese la altura: "))
    area=b*h
    print("-----El area es:", area,"------")

    archivo=open("EJERCICIO_12.txt","a")
    archivo.write("Rectangulo ")
    archivo.write("Base:")
    archivo.write(str(b))
    archivo.write(" Altura:")
    archivo.write(str(h))
    archivo.write(" Area: ")
    archivo.write(str(area))
    archivo.write("\n")
    archivo.close()

def lectura():
    print("Mostrar Historial \n")
    archivo=open("EJERCICIO_12.txt")
    print(archivo.read())
    archivo.close()

    cursor= conexion.cursor()
    SQL = "SELECT*FROM areas;"
    cursor.execute(SQL)
    valores=cursor.fetchall()
    print(valores)
    cursor.close()


while menu!=6:
    if menu==1:
        circulo()
    
    elif menu==2:
        triangulo()
    
    elif menu==3:
        cuadrado()

    elif menu==4:
        rectangulo()
    
    elif menu==5:
        lectura()
    
    else:
        print("Opcion Invalida")
    
    menu=int(input("----BIENVENDO SELECCIONE UNA OPCION---- \n 1- Circulo \n 2- Triangulo \n 3- Cuadrado \n 4- Rectangulo \n 5- Ver datos \n 6- Salir \n"))

conexion.close()

