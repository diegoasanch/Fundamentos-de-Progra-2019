print('Ver en pantalla los numeros contando en pasos ingresados comprendidos entre dos numeros')
print()
a=int(input('Ingrese uno de los limites: '))
b=int(input('Ingrese el otro limite: '))
sep=int(input('Ingrese la cant de separacion entre cada num a imprimir: '))
print()
if a==b:
    print('No ingreso 2 numeros naturales distintos')
elif a>b:
    c=b
    b=a
    a=c
cont=a
while cont<b:
    print(cont,end=',')
    cont=cont+sep
if cont==b:
    print(b)
print()
print('esos son los numeros entre',a,'y',b,'contando cada',sep,'numeros')
    