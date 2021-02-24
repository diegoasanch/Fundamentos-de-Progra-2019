# Realizar un programa que permita ingresar números en una lista, finalizando la
# lectura con -1. Informar si la secuencia de elementos ingresada es ascendente,
# descendente, todos sus valores son iguales o se encuentra desordenada.

# Ingreso de valores
def ingresodenum():
    lista = []
    n=int(input('Ingrese un numero: '))
    while n!=-1:
        if n>=0:
            lista.append(n)
        else:
            print('Error, debe ingresar un numero igual o mayor a 0')
        n=int(input('Ingrese un numero: '))
    return lista

# Verificacion del tipo de lista
# leyenda de tipos 0 = lista desordenanda, 1 = elementos iguales, 2 = lista ascendiente, 3 igual lista descendiente
def tipodelista(lista):
    largo = len(lista)
    #cuando los extremos comienzan iguales
    if lista[0] == lista[largo-1]:
        flag = 1           #señalador que se mantiene en 1 hasta que no sean iguales
        for i in range(largo):
            if lista[0] == lista[i]:
                flag = flag * 1
            else:
                flag = 0
    #cuando el primer valor es menor al ultimo y existe la posibilidad de que sea ascendiente
    elif lista[0] < lista[largo-1]:
        flag = 2
        for i in range(largo-1):
            if lista[i] <= lista[i+1]:
                flag = flag * 1
            else:
                flag = 0
    #cuando existe la posibilidad de ser descendiente
    else:
        flag = 3
        for i in range(largo-1):
            if lista[i] >= lista[i+1]:
                flag = flag * 1
            else:
                flag = 0
    return flag

# Programa principal
print('Cargue numeros N a una lista y vea si la secuencia de sus elementos es \nascendiente, descendiente, sus elementos iguales o desordenanda')
print('Ingrese -1 para finalizar la carga de la lista')
print()
v = ingresodenum()
print()
print(v)
print()
if v == []:
    print('No ingreso ningun elemento')
else:
    tipo = tipodelista(v)
    if tipo == 1:
        print('Todos los elementos de la lista son iguales')
    elif tipo == 2:
        print('La lista es ascendiente')
    elif tipo == 3:
        print('La lista es descendiente')
    else:
        print('La lista esta desordenada')