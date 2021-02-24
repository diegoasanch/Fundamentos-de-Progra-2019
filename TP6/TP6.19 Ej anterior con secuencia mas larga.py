# A partir de la lista SECUENCIAS generada en el ejercicio anterior, imprimir la
# secuencia más larga almacenada en la misma. Si hubiera varias secuencias con
# la misma longitud máxima deberán mostrarse todas las que correspondan.

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
        
# Buscador de la/s secuencia mas larga
def maxsec(v):
    iniciodesec = []
    mayorsec = 0
    for j in range(2):
        sec = 0
        for i in range(len(v)):
            if v[i] != 0:
                sec += 1
            else:
                sec = 0
            if j == 0:                
                if sec > mayorsec:
                    mayorsec = sec
            else:
                if sec == mayorsec:
                    iniciodesec.append(i-(mayorsec - 1))
    print('La secuencia/s mas larga es de',mayorsec,'digitos')
    for i in range(len(iniciodesec)):
        for j in range(mayorsec):
            print(v[iniciodesec[i]+j],end=',')
        print()
    return
    
# programa principal
N = int(input('Cuantos numeros al azar desea cargar a la lista? :'))
SECUENCIAS = cargadelista(N)
print(SECUENCIAS)
maxsec(SECUENCIAS)