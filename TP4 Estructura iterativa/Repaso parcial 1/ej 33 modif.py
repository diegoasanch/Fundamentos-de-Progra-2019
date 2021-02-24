print('Calculo de la raiz cuadrada de un numero')
n=int(input('Ingrese un numero: '))
print('Ingrese el grado de precision con el que desea realizar su calculo')
prec=int(input('1, 2 o 3?: '))
if prec==1:
    prec=0.0001
elif prec==2:
    prec=0.000001
else:
    prec=0.000000001
dif=1
a=n/2
while dif>prec:
    ant=a
    a=((n/a)+a)/2
    dif=ant-a
print('La raiz cuadrada de',n,'es:',a)