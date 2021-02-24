# Escribir una función para devolver la posición que ocupa un valor pasado como parámetro, utilizando búsqueda
# secuencial en una lista desordenada. La función debe devolver -1 si el elemento no se encuentra en la lista.

#Funcion ingreso de numeros
def ingresodenum():
    lista = []
    n=int(input('Ingrese un numero: '))
    while n!=-1:
        if n>=1 and n<=20:
            lista.append(n)
        else:
            print('Error, debe ingresar un numero entre 1 y 20')
        n=int(input('Ingrese un numero: '))
    return lista

#Funcion busqueda de parametro
def busqueda(valor,lista):
    largo = len(lista)
    encontrados = []                 #inicializacion de lista para guardar las posiciones en las que se encuentra el numero
    for i in range(largo):
        if lista[i] == valor:
            encontrados.append(i)    #si el valor se encuentra en alguna posicion, se agrega la posicion a la lista encontrados
    if encontrados == []:              #y si la lista encontrados termina vacia le agrega el -1
        encontrados = -1
    return encontrados
    
#programa principal
print('Ingrese numeros entre el 1 el 20 a una lista y recibala cargada')
milista=ingresodenum()
buscar=int(input('Ingrese el numero a buscar: '))
posiciones=busqueda(buscar,milista)
if posiciones == -1:
    print(posiciones,'El numero ingresado no pertenece a la lista')
else:
    print('El numero',buscar,'aparece en la lista',milista,'en las posiciones',posiciones)