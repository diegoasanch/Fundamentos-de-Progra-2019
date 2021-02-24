# Ingreso de numeros en una lista
def lista(v):
    n = int(input('Ingrese un numero: '))
    while n != -1:
        v.append(n)
        n = int(input('Ingrese un numero: '))
    return v

# Ingreso de opcion si o no
def opcion():
    a = input('¿Si o No? : ')
    while a!= '1' and a!= '0' and a != 'si' and a != 'SI' and a != 'Si' and a!= 'S' and a!= 's' and a != 'no' and a != 'NO' and a != 'No' and a !='n' and a!='N':
        print('¡Opcion invalida!')
        a = input('¿Si o No? : ')
    if a == '1' or a == 'si' or a == 'SI' or a == 'Si' or a == 'S' or a == 's':
        op = 1
    elif a == '0' or a == 'no' or a == 'NO' or a == 'No' or a== 'N' or a == 'n':
        op = 0
    return op

# Ordenador de listas creciente
def ordencrec(v):
    largo = len(v)
    for i in range(largo-1):
        for j in range(i+1,largo):
            if v[i] > v[j]:  #intercambio de valores de la lista de puntajes
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
    return v

# Odenador de listas decreciente
def ordendecrec(v):
    largo = len(v)
    for i in range(largo-1):
        for j in range(i+1,largo):
            if v[i] < v[j]:  #intercambio de valores de la lista de puntajes
                aux = v[i]
                v[i] = v[j]
                v[j] = aux