#Ídem anterior, utilizando búsqueda binaria sobre una lista ordenada

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
def busquedabinaria(valor,lista):
    izq = 0
    der = len(lista)-1
    encontrado = -1
    while izq <= der and encontrado ==-1:
        centro = (izq + der) // 2
        if lista[centro] == valor:
            encontrado = centro
        elif lista[centro] < valor:
            izq = centro + 1
        else:
            der = centro - 1   
    return encontrado

#Funcion ordenar la lista por seleccion
def ordenador(lista):
    largo = len(lista)
    for i in range(largo-1):
        for j in range(i+1, largo):
            if lista[i] > lista[j]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
    return
    
#programa principal
print('Ingrese numeros entre el 1 el 20 y un valor para extraer por medio de la buqueda binaria')
milista = ingresodenum()
print(milista)
ordenador(milista)
print(milista)
buscar=int(input('Ingrese el numero a buscar: '))
pos=busquedabinaria(buscar,milista)
if pos == -1:
    print(pos,'El numero ingresado no pertenece a la lista')
else:
    print('El numero',buscar,'aparece en la lista en la posicion',pos)