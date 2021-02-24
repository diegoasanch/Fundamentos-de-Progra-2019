#Realizar un programa para ingresar desde el teclado un conjunto de números. Al
#finalizar mostrar por pantalla el primer y último elemento ingresado. Finalizar la
#lectura con el valor -1.
print('Ingrese numeros, para finalizar ingrese -1')
print()
n=int(input('Ingrese un valor: '))
if n!=-1:
    primero=n
    while n!=-1:
        ultimo=n
        n=int(input('Ingrese un valor: '))
    print('El primer valor ingresado es',primero,'y el ultimo',ultimo)
else:
    print('Ningun valor fue ingresado')