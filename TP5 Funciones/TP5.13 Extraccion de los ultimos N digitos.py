#  Devolver los últimos N dígitos de un número entero pasado como parámetro. El valor de N también
#  debe ser pasado como parámetro. Devolver el número completo si N es demasiado grande. Ejemplo:
#  ultimosdigitos(12345,3) devuelve 345, y ultimosdigitos(12345,8) devuelve 12345.

#funcion extraer digito
def extraerdigito(entero,extraer):
    cont=1
    digitosinv=0
    while cont <= extraer:
        digitosinv = digitosinv * 10 + (entero % 10) #extraccion de los ultimos digitos pero invertidos
        entero = entero // 10  #y se le quita el ultimo digito al entero para repetir el ciclo
        cont = cont + 1
    digitoscorrectos = inversor(digitosinv)
    return digitoscorrectos

#funcion para invertir el numero extraido
def inversor(n):
    inv=0
    while n>0:
        inv= (inv*10) + n % 10
        n=n//10
    return inv

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
print('Ingrese un numero entero y extraiga los ultimos n digitos de el')
A=verifnum('un numero')              #primer numero
B=verifnum('la cantidad a extraer')  #digitos a extraer
extraido=extraerdigito(A,B)
print(extraido)
