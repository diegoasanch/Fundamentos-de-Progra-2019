# Extraer un dígito de un número entero. La función recibe como parámetros dos
# números enteros, uno será del que se extraiga el dígito y el otro indica qué cifra
# se desea obtener. La cifra de la derecha se considera la número 0. Retornar el
# valor -1 si no existe el dígito solicitado. Ejemplo: extraerdigito(12345,1) devuelve 4,
# y extraerdigito(12345,8) devuelve -1.

#funcion extraer digito
def extraerdigito(entero,extraer,longitud):
    if extraer>(longitud-1):  #si se quiere sacar un numero en una posicion mayor a la longitud 
        digito = -1           #del entero, deuelve -1
    else:
        cont=0
        while cont <= extraer:
            digito = entero % 10   #se extrae uno por uno el ultimo digito, hasta llegar al deseado
            entero = entero // 10  #y se le quita el ultimo digito al entero para repetir el ciclo
            cont = cont + 1
    return digito

#funcion determina longitud del numero
def longitudentero(entero):
    cont=0
    while entero>0:
        cont = cont + 1
        entero = entero // 10
    return cont

#verificador de positividad de un numero
def verifnum(tipo):
    print('>>> Ingrese',tipo,': ',end='')
    n=int(input())
    while n<0:
        print('\nNo ingreso un numero valido!!!')
        print('>>> Ingrese',tipo,': ',end='')
        n=int(input())
    return n

#programa principal
print('Ingrese un numero entero y extraiga el numero que este en la posicion del segundo')
print('numero ingresado, contando desde 0, de derecha a izquierda')
A=verifnum('un numero')              #primer numero
B=verifnum('la posicion a extraer')  #digito a extraer
largo=longitudentero(A)
extraido=extraerdigito(A,B,largo)
print(extraido)