
"""Pedir un numero y mostrar sus divisores (valores exactos
que dividen al numero en partes exactas) """


numero=int(input("Ingres el numero: "))
x=1
for n in range(numero):
    
    if (numero%x==0):
        print(x)
    x=x+1
