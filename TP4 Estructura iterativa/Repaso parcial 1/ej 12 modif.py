print('Calculador del producto de dos numeros por sumas sucesivas')
Aneg=0 #indicadores de negatividad
Bneg=0 #para multiplicar por negativos
a=int(input('Ingrese un numero: '))
A=a
if A<0:
    A=A*(-1)
    Aneg=1
b=int(input('Ingrese el otro num: '))
B=b
if B<0:
    B=B*(-1)
    Bneg=1
if (A or B)==0:
    print(a,'*',b,'= 0')
else:
    prod=0
    cont=1
    while cont<=B:
        prod=prod+A
        cont=cont+1
if (Aneg==1 and Bneg!=1) or (Aneg!=1 and Bneg==1):
    prod=prod*(-1)
print()
print(a,'*',b,'=',prod)
    