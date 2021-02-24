# Desarrollar la función signo(n), que reciba un número entero y devuelva un 1, -1
# o 0 según el valor recibido sea positivo, negativo o nulo.
def signo(n):
    if n>0:
        v=1
        valor='positivo'
    elif n<0:
        v=-1
        valor='negativo'
    else:
        v=0
        valor='nulo'
    return v,valor
#programa principal
print('ingrese un numero y reciba 1, -1 o 0 segun el valor recibido \nsea positivo, negativo o nulo')
N=int(input('Ingrese un numero entero: '))
recibido,tipo = signo(N)
print(recibido,'el numero ingresado es',tipo)