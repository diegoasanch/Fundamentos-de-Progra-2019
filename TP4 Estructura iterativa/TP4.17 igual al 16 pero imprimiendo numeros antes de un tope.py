#Para las mismas series del ejercicio anterior, informar el término de mayor valor
#que sea menor a un tope ingresado previamente. Ejemplo: Para las series a), b)
#y c), si se ingresa el valor 10 como tope se deberá informar 9, 10 y 7 respectivamente.
print('Para las series del ej anterior informar el termino de mayor valor que sea menor a un tope definido')
tope=int(input('Ingrese el tope: '))
start=input('Presione enter para comenzar')
print()
cont=0
topeA=0
print('a)')
while cont<10:  #a
    A2=2**cont
    A3=3**cont
    print('2^'+str(cont)+'=',A2,',','3^'+str(cont)+'=',A3)
    cont=cont+1
    if A2<=tope and A2>topeA:     #Almacenamiento de mayor numero menor al tope
        topeA=A2
    if A3<=tope and A3>topeA:
        topeA=A3
print('El termino de mayor valor antes de',tope,'en a fue de=',topeA)
cont=1
topeB=0
print()
print('b)')
while cont<=20:  #b
    B=cont*(-1)**cont
    print(str(cont)+'*(-1)^'+str(cont)+'=',B)
    cont=cont+1
    if B<=tope and B>topeB:
        topeB=B
print('El termino de mayor valor antes de',tope,'en b fue de=',topeB)
cont=1
C=1
topeC=0
print()
print('c)')
print(cont)
while cont<20:   #c
    C=cont+C
    print(str(cont)+'+'+str(C)+'=',C)
    cont=cont+1
    if C<=tope and C>topeC:
        topeC=C
print('El termino de mayor valor antes de',tope,'en c fue de=',topeC)
    