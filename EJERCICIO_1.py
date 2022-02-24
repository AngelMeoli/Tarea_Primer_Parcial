"""Pedir 3 numeros:
Si el primero es el mas grande mosntrar a suma de los tres numeoros.
Si el segundo es el mas grande mostrar la multiplicacion de los 3 numeros.
Si el tercero es el mas grande concatenar los tres numeros.
Si los tres son iguaes mostrar los numeros y el mensaje: Todos son iguales"""

a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el terce numero: "))



if (a==b and a==b and b==c):
    print("Todos son iguales")

if((a==b or a==c or c==b) and (a!=b or a!=c or c!=b )):
    if(a==b):
        print("El primer y segundo numero son iguales!")
        
    if(a==c):
        print("El primer y tercer numero son iguales!")
        
    if(b==c):
        print("El segundo y tercer numero son iguales!")
        

if a!=b and a!=c and c!=b:

    if a>b and a>c:
        print("El primer numero es el mayor. ","La suma de los tres numeros es: ",str(a+b+c))

    if b>a and b>c:
        print("El segundo numero es el mayor. ","La multiplicacion de los tres numeros es: ",str(a*b*c))

    if c>a and c>b:
        print("El tercer numero es el mayor. ","La concatenacion de los tres numeros es: ",str(a)+str(b)+str(c))







