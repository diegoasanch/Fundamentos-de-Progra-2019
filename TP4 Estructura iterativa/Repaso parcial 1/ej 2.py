print('Ingresar numeros y ver por pantalla el primero y ultimo ingresados, finaliza con -1')
n=int(input('Ingrese un numero: '))
if n!=-1:
    primer=n
    ultimo=n
    while n!=-1:
        ultimo=n
        n=int(input('Ingrese un numero: '))
    print()
    print('El primer numero ingresado fue',primer)
    print('Y el ultimo',ultimo)
else:
    print('No ingreso ningun numero')