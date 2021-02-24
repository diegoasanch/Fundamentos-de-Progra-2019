print('TP4 ejercicio 16, Imprime los primeros 20 terminos de cada secuencia')
start=input('Presione enter para comenzar')
print()
cont=0
print('a)')
while cont<10:  #a
    A2=2**cont
    A3=3**cont
    print('2^'+str(cont)+'=',A2,',','3^'+str(cont)+'=',A3)
    cont=cont+1
cont=1
print()
print('b)')
while cont<=20:  #b
    b=cont*(-1)**cont
    print(str(cont)+'*(-1)^'+str(cont)+'=',b)
    cont=cont+1
cont=1
print()
print('c)')
print(cont)
c=1
while cont<20:
    c=cont+c
    print(str(cont)+'+'+str(c)+'=',c)
    cont=cont+1