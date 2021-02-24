print('Ingrese numero y vea por pantalla el menor y mayor de ellos, -1 para salir')
print()
n=int(input('Ingrese un numero: '))
if n==-1:
    print()
    print('*No ingreso ningun numero*')
else:
    menor=n
    mayor=n
    while n!=-1:
        if n<menor:
            menor=n
        elif n>mayor:
            mayor=n
        n=int(input('Ingrese un numero: '))
    print()
    if mayor==menor:
        print('Se ingreso un unico numero:',mayor)
    else:
        print('El mayor numero fue:',mayor,'y el menor:',menor)