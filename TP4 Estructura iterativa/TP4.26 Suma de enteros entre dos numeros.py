#Calcular e imprimir la suma de los números enteros comprendidos entre dos
#números enteros A y B ingresados por teclado. Tener en cuenta que A puede ser
#mayor, menor o igual que B.
print('Calcular la suma de los numeros enteros comprendidos entre dos numeros enteros')
A=int(input('Ingrese el valor de A: '))
B=int(input('Ingrese el valor de B: '))
if A<=B:
    A=A
    B=B
else:
    C=B
    B=A
    A=C
cont=A+1
suma=0
while cont<B:
    suma=suma+cont
    cont=cont+1
print('La suma de los enteros comprendidos entre',A,'y',B,'es de=',suma)