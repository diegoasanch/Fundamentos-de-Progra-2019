# Calcular la suma de los números de una lista.

# funcion ingreso de numeros dentro del rago 
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

#funcion suma de la lista
def sumadelista(lista):
    largo =len(lista)
    suma=0
    for i in range(largo):
        suma=suma+lista[i]
    return suma

#programa principal
print('Ingrese numeros entre el 1 el 20 a una lista y reciba la suma de los valores ingresados')
milista = ingresodenum()
listasumada = sumadelista(milista)
print('Lista ingresada',milista,'Suma de los elementos de la lista=',listasumada)