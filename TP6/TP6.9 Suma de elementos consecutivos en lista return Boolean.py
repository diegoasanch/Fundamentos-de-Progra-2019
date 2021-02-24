# Dado una lista de N números (por ejemplo 5), devolver una lista de N-1 valores booleanos, tal que cada valor de este último
# arreglo corresponde al resultado de la comparación de los pares de valores consecutivos del primer arreglo. El valor
# booleano es True si el primer elemento del par es menor o igual que el siguiente, y False si no lo es.
import random

def cargar():
    v = []
    n=int(input('Ingrese la cantitad de elementos que desea generar: '))
    for i in range(n):
        v.append(random.randint(0,100))
    return v

def verifb(v):
    vb = []
    for i in range(len(v)-1):
        if (v[i] + v[i+1]) % 2 == 0:
            vb.append(True)
        else:
            vb.append(False)
    return vb
# programa principal
print('Generar en una lista elementos al azar y reciba V si la suma de los valores consecutivos es o F si es impar')
lista = cargar()
listabooleana = verifb(lista)
print(lista)
print(listabooleana)