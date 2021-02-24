print('Ultimo numero ingresado en una posicion par')
n=int(input('Ingrese un numero: '))
cont=1
if n==-1:
    print('No se ingreso ningun numero')
else:
    while n!=-1:
        if cont%2==0:
            ultimop=n
        n=int(input('Ingrese un numero: '))
        cont=cont+1
    print()
    print('El ultimo numero ingresado en una posicion par fue:',ultimop)