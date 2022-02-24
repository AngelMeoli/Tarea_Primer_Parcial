
"""Pedir un número de inicio y un número de fin y mostrar los números de 2 en 2 desde el número de 
    inicio hasta el numero de fin."""

inicio=int(input("Ingrese el numero de inicio: "))
ultimo=int(input("Ingres el numero final: "))
print("Ingreso: ",str(inicio),"y",str(ultimo))
print("Resultado:", end=" ")
for c in range(inicio,ultimo+1,2):
    print(c, end=",")


