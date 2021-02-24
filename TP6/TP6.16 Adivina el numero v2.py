# Desarrollar un programa que genere un número entero al azar de cuatro cifras y proponerle al usuario que lo descubra,
# ingresando valores repetidamente hasta hallarlo. En cada intento el programa mostrará mensajes indicando si el
# número ingresado es mayor o menor que el valor secreto. Permitir que el usuario abandone al ingresar -1. Informar
# la cantidad de intentos realizada al terminar el juego, haciendo que el usuario ingrese su nombre si mejoró la mejor
# marca de intentos obtenida hasta el momento. Luego mostrar la lista de los 5 mejores puntajes y preguntar si se
# desea jugar otra vez, reiniciando el juego en caso afirmativo.

import random

# Instrucciones
def instrucciones():
    print('¿Desea leer las instrucciones del juego?')
    op = ingresodeopcion()
    if op == 1:
        print('\n+----------+----------+----------+----------+----------+----------+----------+----------+----------+')
        print('             El juego consiste en adivinar un numero al azar generado por la computadora')
        print('  Las opciones posibles estan entre el 1000 y el 9999, si tu numero ingresado no es el valor secreto')
        print('   el programa te informara si estas adivinando un numero mayor o menor para que adivines de nuevo.')
        print('          Si deseas abandonar la partida sin terminarla ingresa el numero -1. ¡Buena suerte!')
        print('+----------+----------+----------+----------+----------+----------+----------+----------+----------+\n')
        input('Presione enter para comenzar el juego ')
    print()
    return

# Generacion de Numero al azar, desde 1000, hasta 9999
def generador():
    return random.randint(1000,9999)

# Juego
def busquedadelnum(mejoresp,mejoresn):
    rand = generador()
    cont = 0
    guess = int(input('>Ingrese su numero: '))
    while guess != rand and guess != -1:
        if guess < 1000 or guess >9999:
            print('Numero invalido, recuerda que el numero debe estar entre 1000 y 9999, intenta de nuevo')
        else:
            if guess < rand:
                print('Su numero es MENOR al valor secreto')
            else:
                print('Su numero es MAYOR al valor secreto')
            cont += 1
        guess = int(input('Ingrese su numero: '))
    if guess == -1:
        print('\n*** Partida abandonada despues de',cont,'intentos\n')
    else:
        cont +=1
        print('\n¡Has adivinado el valor secreto! :',rand)
        print(' Te tomo',cont,'intentos\n')
        mejorespunt(mejoresp,mejoresn,cont)
            
# Tabla de mejores puntajes
def mejorespunt(puntos,nombres,puntaje):
    if len(puntos)==1 or puntaje < puntos[1]:
        print('¡Has establecido un nuevo record!\n')
    elif puntaje == puntos[1]:
        print('¡Has igualado el mejor puntaje!\n')
    nombre = input('Ingresa tu nombre para cargarlo a la leaderboard: ')
    puntos.append(puntaje)
    nombres.append(nombre)
    ordenador(puntos,nombres)
    if len(puntos) < 6:
        largo = len(puntos)
    else:
        largo = 6
    print('\n+----------+----------+----------+')
    if largo -1 == 1:
        print('           Unico puntaje')
    else:
        print('       Mejores',largo-1,'puntajes')
    print('    Puntos              Jugador')
    for i in range(1,largo):
        nombre = nombres[i]
        print('    ',puntos[i],'----------------',nombre.capitalize())
    print('+----------+----------+----------+')
    print()
    return   
        
# Ordenador de lista de forma ascendiente por el metodo de seleccion
def ordenador(puntos,nombres):
    largo = len(puntos)
    for i in range(largo-1):
        for j in range(i+1,largo):
            if puntos[i] > puntos[j]:  #intercambio de valores de la lista de puntajes
                aux = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = aux
                # Intercambio de nombres en la posicion correspondiente al puntaje
                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux
                
    return
        
# Opcion reintentar, Ingresa por teclado la opcion de reintentar el juego
def ingresodeopcion():
    a = input('¿Si o No? : ')
    while a!= '1' and a!= '0' and a != 'si' and a != 'SI' and a != 'Si' and a!= 'S' and a!= 's' and a != 'no' and a != 'NO' and a != 'No' and a !='n' and a!='N':
        print('¡Opcion invalida!')
        a = input('¿Si o No? : ')
    if a == '1' or a == 'si' or a == 'SI' or a == 'Si' or a == 'S' or a == 's':
        op = 1
    elif a == '0' or a == 'no' or a == 'NO' or a == 'No' or a== 'N' or a == 'n':
        op = 0
    return op
    
#Programa principal
print('¡Adivina el valor secreto!')
print()
option = 1
instrucciones()
punt, nomb = [0],[0] # Inicializacion de las listas de puntajes
while option == 1:
    busquedadelnum(punt,nomb)
    print('¿Desea volver a jugar?')
    option = ingresodeopcion()
    print()
print('Gracias por jugar Adivina el valor secreto :)')