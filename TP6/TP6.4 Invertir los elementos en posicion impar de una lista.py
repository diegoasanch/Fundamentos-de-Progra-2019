# Invertir aquellos valores ubicados en posiciones impares de una lista.
#funcion ingreso de numeros TP6.1
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

#Funcion invertir
def invertirlista(lista):
    largo = len(lista)
    if largo%2 == 0:         #si la lista tiene una cantidad par de numeros comenzamos desde el penultimo
        pos = largo - 1      #ya que el numero de orden del ultimo elemento es el largo -1 y por lo tanto ese seria impar
    else:
        pos = largo - 2      #y si tiene una cantidad impar comenzamos desde el ante-penultimo
    hasta = largo//2         #llegamos hasta la mitad de la lista porque si no la invertiriamos de nuevo y quedaria igual
    for i in range(1,hasta,2): 
        temporal = lista[i]         #intercambio de valores con el auxiliar temporal
        lista[i]= lista[pos]
        lista[pos] = temporal
        pos=pos-2
    return lista
    
#programa principal
print('Ingrese numeros entre el 1 el 20 a una lista e invertir los elementos ubicados en posiciones impares')
milista=ingresodenum()
print('La lista',milista,end=' ')
milista_imp_inv=invertirlista(milista)
print ('con los elementos ingresados en posicion impar invertidos es',milista_imp_inv)