# : Ingresar por teclado un número N y construir una lista llamada SECUENCIAS con
# N números enteros al azar entre 1 y 20. Esta lista se caracterizará porque sus
# valores deben encontrarse divididos en secuencias de números separadas por
# ceros, cuya suma no sea mayor que 20. Para eso se deberá agregar un elemento
# de valor 0 a fin de separar cada secuencia de la siguiente, cuidando que ninguna
# secuencia sume más de 20. Agregar un 0 adicional al final de la lista y mostrar la
# lista obtenida por pantalla.

import random

#Carga de numeros al azar a la lista
def cargadelista(n):
    v = []
    suma = 0
    for i in range(n):
        x = random.randint(1,20)
        suma += x
        if suma <= 20:
            v.append(x)
        else:
            v.append(0)
            v.append(x)
            suma = x
    return v
        
# programa principal
N = int(input('Cuantos numeros al azar desea cargar a la lista? :'))
SECUENCIAS = cargadelista(N)
print(SECUENCIAS)