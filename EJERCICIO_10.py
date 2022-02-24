"""Pedir dos números, verificar cuál es el mayor y mostrar la lista de números desde el mayor hasta el menor."""


dato1=int(input("Ingrese un numero: "))
dato2=int(input("Ingres un numero: "))

if dato1>dato2:
    inicio=dato1
    ultimo=dato2

elif dato1<dato2:

    inicio=dato2
    ultimo=dato1

else:
    print("los numeros son iguales")

    
print("Ingreso: ",str(dato1),"y",str(dato2))

print("Resultado:", end=" ")
try:
    for c in range(ultimo,inicio+1,1):
        b=inicio
        print(b, end=",")
        inicio=inicio-1
except NameError:
    print("Vuelva a intentarlo")