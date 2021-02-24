#Para las mismas series y topes del ejercicio anterior, informar el resultado de la
#sumatoria de los términos calculados hasta cada tope.
print('Para las series del ej anterior informar la sumatoria de los terminos calculados hasta cada tope')
tope=int(input('Ingrese el tope: '))
print()
cont=0
topeA=0
sumaA=0
print('a)')
while cont<10:  #a
    A2=2**cont
    A3=3**cont
    print('2^'+str(cont)+'=',A2,',','3^'+str(cont)+'=',A3)
    cont=cont+1
    if A2<=tope and A2>=topeA:             #Almacenamiento de mayor numero menor al tope
        topeA=A2
        sumaA=sumaA+A2                     #suma de los calculados antes del tope
    if A3<=tope and A3>=topeA:
        topeA=A3
        sumaA=sumaA+A3 #suma de los calculados antes del tope
print('El termino de mayor valor antes de',tope,'en a fue de=',topeA)
print('La suma de todos los terminos calculados hasta',tope,'es de=',sumaA)
cont=1
topeB=0
sumaB=0
print()
print('b)')
while cont<=20:  #b
    B=cont*(-1)**cont
    print(str(cont)+'*(-1)^'+str(cont)+'=',B)
    cont=cont+1
    if B<=tope and B>topeB:               #Almacenamiento de mayor numero menor al tope
        topeB=B
    if B<=tope and -B<tope:
        sumaB=sumaB+(B)                   #suma de los calculados antes del tope
print('El termino de mayor valor antes de',tope,'en b fue de=',topeB)
print('La suma de todos los terminos calculados hasta',tope,'es de=',sumaB)
cont=1
C=1
topeC=0
sumaC=1
print()
print('c)')
print(cont)
while cont<20:   #c
    C=cont+C
    print(str(cont)+'+'+str(C)+'=',C)
    cont=cont+1
    if C<=tope and C>topeC:                  #Almacenamiento de mayor numero menor al tope
        topeC=C
        sumaC=sumaC+C
print('El termino de mayor valor antes de',tope,'en c fue de=',topeC)
print('La suma de todos los terminos calculados hasta',tope,'es de=',sumaC)