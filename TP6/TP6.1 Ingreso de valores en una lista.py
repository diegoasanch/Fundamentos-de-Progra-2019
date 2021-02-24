# Escribir una función para ingresar desde el teclado una serie de números entre 1 y 20 y guardarlos en una lista.
# En caso de ingresar un valor fuera de rango el programa mostrará un mensaje de error y solicitará un nuevo número.
# Para finalizar la carga se deberá ingresar -1. La función no recibe ningún parámetro, y devuelve la lista cargada
# (o vacía, si el usuario no ingresó nada) como valor de retorno.

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

#programa principal
print('Ingrese numeros entre el 1 el 20 a una lista y recibala cargada')
milista=ingresodenum()
print(milista)