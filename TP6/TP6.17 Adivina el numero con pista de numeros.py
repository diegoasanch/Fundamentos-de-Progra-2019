# Modificar el programa anterior para que las pistas brindadas por el programa no
# sean del tipo "es mayor" o "es menor" sino "M dígitos correctos y N dígitos
# aproximados". Se considera que un dígito es correcto cuando tanto su valor
# como su posición coinciden con los del número secreto, mientras que un dígito
# es aproximado cuando coincide el valor pero no su posición. Ejemplos:
# Número secreto: 5739
# · Intento 1: 1234 -> 1 correcto
# · Intento 2: 5678 -> 1 correcto y 1 aproximado
# · Intento 3: 9375 -> 4 aproximados

import random
import Basiclib
# Instrucciones
def instrucciones():
    print('¿Desea leer las instrucciones del juego?')
    op = ingresodeopcion()
    if op == 1:
        print('\n+----------+----------+----------+----------+----------+----------+----------+----------+----------+')
        print('             El juego consiste en adivinar un numero al azar generado por la computadora')
        print('  Las opciones posibles estan entre el 1000 y el 9999, si tu numero ingresado no es el valor secreto')
        print('   el programa te informara cuantos digitos tienes correctos (valor y posicion correctos) y cuantos.')
        print('                 digitos tienes aproximados (valor correcto pero posicion diferente)')
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
    randlist = pasar_a_lista(rand)
    cont = 1
    guess = int(input('>Ingrese su numero: '))
    while guess != rand and guess != -1:
        if guess < 1000 or guess >9999:
            print('Numero invalido, recuerda que el numero debe estar entre 1000 y 9999, intenta de nuevo')
        else:
            cont += 1
            pista(randlist,guess)
        print('>Intento',cont,':',end=' ')
        guess = int(input())
    if guess == -1:
        print('\n*** Partida abandonada despues de',cont,'intentos\n')
    else:
        print('\n¡Has adivinado el valor secreto! :',rand)
        print(' Te tomo',cont,'intentos\n')
        mejorespunt(mejoresp,mejoresn,cont)
            
def pista(n,guess):
    guesslist = pasar_a_lista(guess)
    correcto = 0
    aprox = 0
    for i in range(4):
        if guesslist[i] == n[i]:
            correcto += 1
        for j in range(4):
            if guesslist[i] == n [j] and i != j:
                aprox += 1
    print(correcto,'correctos',aprox,'aproximados')
    return
 

#devuelve el numero ingresado como digistos separados en una lista  
def pasar_a_lista(n):
    v = []
    while n > 0:
        resto = n % 10
        n = n // 10
        v.append(resto)
    return v
    
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