"""Pedir una palabra y contar cuantas vocales tiene"""

palabra=input("Ingrese una palabra: ")
contador=0
for c in palabra:
    if(c=="a" or c=="e" or c=="i" or c=="o" or c=="u"):
        contador=contador+1

print("La palabra tiene ",str(contador), " vocales")