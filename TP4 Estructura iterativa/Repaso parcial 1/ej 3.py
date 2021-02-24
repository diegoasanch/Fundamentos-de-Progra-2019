print('Cantidad de numeros par o impar sin contadores, ingrese -1 para termnar')
n=int(input('Ingrese un numero: '))
if n!=-1:
    ind=1    #ind = indicador
    while n!=-1:
        ind=ind*(-1)
        n=int(input('Ingrese un numero: '))
    print()
    if ind==-1:
        print('Se ingreso una cantidad impar de numeros')
    else:
        print('Se ingreso una cantidad par de numeros')
else:
    print('No ingreso ningun numero')