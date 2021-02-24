print('Ver en pantalla los numeros naturales comprendidos entre dos numeros')
print()
a=int(input('Ingrese uno de los limites: '))
b=int(input('Ingrese el otro limite: '))
print()
if a==b:
    print('No ingreso 2 numeros naturales distintos')
elif a>b:
    c=b
    b=a
    a=c
cont=a+1
while cont<b:
    print(cont,end=',')
    cont=cont+1
print()
print('esos son los numeros naturales entre',a,'y',b)
    