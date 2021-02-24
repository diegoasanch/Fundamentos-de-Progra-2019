# Adaptar el programa que utiliza la fórmula de Newton para calcular la raíz cuadrada de un número positivo N
# (de la práctica anterior) para que trabaje como una función.
#funcion raiz cuadrada
def calculoraiz(n):
    a=(n/2)
    dif=1
    while dif > 0.00001:
        raiz=((n/a)+a)/2
        dif=a-raiz
        a=raiz
    return raiz

#verificador de positividad de un numero
def verifnum():
    n=int(input('>>> Ingrese un numero positivo: '))
    while n<=0:
        print('\nNo ingreso un numero valido!!!')
        n=int(input('>>> Ingrese un numero positivo: '))
    return n

#programa principal
print('Calculo de raiz cuadrada de un numero usando la formula de Newton')
N = verifnum()
resultado = calculoraiz(N)
print('La raiz cuadrada de',N,'es',resultado)