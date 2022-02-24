
"""Pedir un numero y mostrar la suma de los nuemros desde 0 
hasta ese numero"""

numero=int(input("Ingrese su numero: "))
b=0
for c in range(numero+1):
    b=c+b
print("Resultado: ",str(b))