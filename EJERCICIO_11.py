"""Pedir una palabra y contar cuántas veces aparece cada vocal."""
palabra=input("Ingres una palabra: ")
cont1, cont2, cont3, cont4, cont5 =0,0,0,0,0
for c in palabra:
    if c=="a":
        cont1=cont1+1
    if c=="e":
        cont2=cont2+1
    if c=="i":
        cont3=cont3+1
    if c=="o":
        cont4=cont4+1
    if c=="u":
        cont5=cont5+1
print("A=", str(cont1))
print("E=", str(cont2))
print("I=", str(cont3))
print("O=", str(cont4))
print("U=", str(cont5))