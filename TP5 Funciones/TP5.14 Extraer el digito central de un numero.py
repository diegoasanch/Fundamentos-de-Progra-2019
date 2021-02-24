# Obtener el dígito central de un número entero pasado como parámetro, sólo si la
# cantidad de dígitos es impar. Si la longitud fuera par devolver -1. Ejemplo:
# digitocentral(12345) devuelve 3, y digitocentral(123456) devuelve -1.

#funcion extraer digito
def extraerdigito(entero,longitud):
    if longitud % 2 == 0:     #si el numero ingresado es par 
        digito = -1           #deuelve -1
    else:
        extraer = ((longitud-1)/2)+1
        cont=1
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
print('Ingrese un numero entero y si tiene una cantidad impar de digitos, extrae el central')
A=verifnum('un numero')              #ingreso del numero
largo=longitudentero(A)
extraido=extraerdigito(A,largo)
print(extraido)