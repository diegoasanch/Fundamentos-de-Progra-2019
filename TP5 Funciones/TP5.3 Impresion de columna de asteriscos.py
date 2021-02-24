# Imprimir una columna de asteriscos, donde su altura se recibe como parámetro

#funcion de impresion
def imprimircolumna(h):
    while h>0:
        print('*')
        h=h-1
    return

#verificador de positividad de un numero
def verifnum(tipo):
    print('>>> Ingrese',tipo,': ',end='')
    n=int(input())
    while n<0:
        print('\n****Ingrese un numero >=0****')
        print('>>> Ingrese',tipo,': ',end='')
        n=int(input())
    return n

#programa principal
print('Imprimir una columna de asteriscos con la altura ingresada')
A=verifnum('la altura') #ingreso del parametro
columna= imprimircolumna(A)
print('La columna tiene una altura de',A,'asteriscos')