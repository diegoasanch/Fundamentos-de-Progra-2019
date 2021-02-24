#  Verificar si un número es par o impar, devolviendo True o False respectivamente.
def paroimpar(numero):
    if numero%2==0:
        paridad=True
    else:
        paridad=False
    return paridad
#Programa principal
print('Verificar si un numero es par o impar')
n=int(input('Ingrese un numero: '))
par= paroimpar(n)
print('El numero',n,'es par:',par)