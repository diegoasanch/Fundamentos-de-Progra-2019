#  Calcular el Máximo Común Divisor de dos enteros no negativos, basándose en
#  las siguientes fórmulas matemáticas:
#   · MCD(X,X) = X
#   · MCD(X,Y) = MCD(Y,X)
#   · Si X > Y => MCD(X,Y) = MCD(X-Y,Y).
#  Ejemplo: MCD(40,15) devuelve 5.

#verificador de positividad de un numero
def verifnum():
    n=int(input('Ingrese un numero: '))
    while n<=0:
        print('\nDebe ingresar un entero positivo!!!')
        n=int(input('Ingrese un numero: '))
    return n

# Programa de validacion que envia a MCD
def validacion(X,Y):
    if X==Y:
        Maximo=X 
    else:
        while X!=Y:             
            if X > Y:
                X = X-Y
            else:                 # Si X es menor a Y, intercambiamos posiciones para realizar la resta de nuevo
                temp = Y          # hasta hacerlos llegar al mismo valor
                Y = X
                X = temp
        Maximo = X 
    return Maximo
    
#programa principal
print('Calculo del Maximo Comun Divisor (MCD) de dos numeros enteros positivos')
print()
A=verifnum()
B=verifnum()
MCD=validacion(A,B)
print('El MCD de',A,'y',B,'es:',MCD)