# Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir el valor mínimo y el lugar
# que ocupa. Tener en cuenta que el mínimo puede estar repetido, en cuyo caso deberán mostrarse todas las
# posiciones que ocupe. La carga de datos termina cuando se obtenga un 0 como número al azar, el que
# no deberá cargarse en la lista.

import random

# Funcion carga de valores
def cargadevalores():
    numeros = []
    n = random.randint(0,100)
    while n!=0:
        numeros.append(n)
        n = random.randint(0,100)
    return numeros

# Funcion busqueda de minimo y maximo valor
def busquedamaxmin(v):
    men = v[0]
    may = v[0]
    largo = len(v)
    for i in range(largo):
        if v[i] > may:
            may = v[i]
        elif v[i] < men:
            men = v[i]
    menores = []
    mayores = []
    for j in range(largo):
        if v[j] == may:
            mayores.append(j)
        elif v[j] == men:
            menores.append(j)
    return men, may, menores, mayores
    

# Programa principal
print('Rellenar una lista con numeros enteros entre 0 y 100 generados al azar e imprimir el minimo y malximo y su respectivo lugar en la lista')
lista = cargadevalores()
if lista == []:
    print('#########################################################################################################')
    print('****El generador de numeros aleatorios fallo en su unica tarea y el primer elemento generado fue 0 :(****')
    print('#########################################################################################################')
else:
    print(lista)
    menor, mayor,Pmenor, Pmayor = busquedamaxmin(lista)
    print('El menor numero de la lista es el',menor,' se encuentra en la posicion/es',Pmenor)
    print('Y el mayor es el',mayor,' y esta en la posicion/es',Pmayor)
