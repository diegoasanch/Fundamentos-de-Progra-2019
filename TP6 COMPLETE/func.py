# Funciones escenciales para la ejecucion de los ejercicios del Trabajo Practico 6: Listas
# A continuacion un listado de las funciones incluidas marico el que lo lea junto con las
# instrucciones de parametros de entrada y retorno:

# 1 - carganormal() [return v] Carga de numeros enteros distintos de (-1) a una lista la carga de datos termina al ingresar el numero (-1), la funcion no recibe ningun parametro y devuelve la lista generada y cargada
# 2 - cargaconlimites(mi,ma) [return v]  Carga de numeros enteros igual que el item 1, pero con limite inferior y limite superior de valores permitidos, la funcion debe recibir esos limites en ese orden y devuelve la lista cargada
# 3 - cargarandom(n,mi,ma) [return v]
# 3.1 - cargarandomhasta0(mi,ma) [return v]
# 4 - inicializacion(n) [return v]
# 5 - acumuladorlista(n,v) []
# 6 - busquedamaxmin(v) [return mi,ma]
# 7 - verifcapicua(v) [return capicua (True/False)]
# 8 - sumadelista(v) [return suma]
# 8.1 - suma_extremos(v) [return vsuma]
# 8.2 - productodelista(v) [return prod]
# 9 - invertirposimpar(v) []
# 10 - busquedasecuencial(n,v) [return enc]
# 10.1 busquedasecuenciallist(n,v) [return enc(list)]
# 11 - ordenadorsecuencial(v) []
# 12 - ordenadorburbujeo(v) []
# 12.1 - ordenadorburbujeodes(v) []
# 13 - busquedabinaria(n,v) [return enc]
# 14 - eliminacion_v1menosv2(v1,v2) []
# 14.1 - eliminaciondereps(v) [return deleted]
# 15 - impresion(v) []
# 15.1 - impresion_laterales(v,vlats) []
# 16 - impresioncumple(v) []
# 16.1 - impresionmeses_max(v,n) []
# 17 - comp_menorigual(v) [return b(lista)]
# 18 - deteccion_de_orden(v) [return tipo] 
# 19 - insercion_ordenada(n,v) []
# 20 - separacion_par_impar(v) [return vpar, vimp]
# 21 - comparacion_laterales(v) [returns vlats]
# 22 - intercalador(v1,v2) [return v3]
# 23 - secuencias(n) [return v]
# 24 - secuencia_mas_larga(v) [return longersec, sec_start (list)]
# 25 - impresiondesec(v,start,length) []
import random

# 1
def carganormal(): #
    v = []
    n = int(input('Ingrese un numero: '))
    while n!= -1:
        v.append(n)
        n = int(input('Ingrese un numero: '))
    return v

# 2
def cargaconlimites(mi,ma): #
    v = []
    n = int(input('Ingrese un numero: '))
    while n!= -1:
        if n >= mi and n <= ma:
            v.append(n)
        else:
            print('***Numero invalido*** debe ingresar un numero entre',mi,'y',ma)
        n = int(input('Ingrese un numero: '))
    return v
   
# 3
def cargarandom(n,mi,ma): #
    v = []
    for i in range(n):
        v.append(random.randint(mi,ma))
    return v

# 3.1
def cargarandomhasta0(mi,ma):
    v = []
    x = random.randint(mi,ma)
    while x != 0:
        v.append(x)
        x = random.randint(mi,ma)
    return v

# 4 Inicializa una lista con tantos 0 ordene el parametro enviado (para usar lista como acumulador)
def inicializacion(n): #
    v = []
    for i in range(n):
        v.append(0)
    return v

# 5
def acumuladorlista(n,v): #
    v[n] = v[n]+1

# 6
def busquedaminmax(v): #
    mi = v[0]
    ma = v[0]
    for i in range(len(v)):
        if v[i] > ma:
            ma = v[i]
        if v[i] < mi:
            mi = v[i]
    return mi , ma

# 7
def verifcapicua(v): #
    capicua = True
    i = 0
    j = len(v)-1
    while capicua and i < (len(v)//2):
        if v[i] != v[j]:
            capicua = False
        i += 1
        j -= 1
    return capicua

# 8
def sumadelista(v): #
    suma = 0
    for i in range(len(v)):
        suma = suma + v[i]
    return suma

# 8.1
def suma_extremos(v):
    vsuma = []
    ext = len(v)
    for i in range(len(v)//2):
        ext = ext - 1
        vsuma.append(v[i]+v[ext])
    if len(v) % 2 != 0:
        vsuma.append(v[len(v)//2])
    return vsuma

# 8.2
def productodelista(v):
    prod = 1
    for i in range(len(v)):
        prod = prod * v[i]
    return prod 

# 9
def invertirposimpar(v): #
    if len(v)%2 == 0:
        j = len(v) - 1
    else:
        j = len(v) - 2
    for i in range(1,len(v)//2,2):
        aux = v[i]
        v[i] = v[j]
        v[j] = aux
        j -= 2

# 10
def busquedasecuencial(n,v): #
    enc = -1
    for i in range(len(v)):
        if v[i] == n:
            enc = n
    return enc

# 10.1
def busquedasecuenciallist(n,v): #
    enc = []
    for i in range(len(v)):
        if v[i] == n:
            enc.append(i+1)
    return enc

# 11
def ordenadorsecuencial(v): #
    for i in range(len(v)-1):
        for j in range(i,len(v)):
            if v[i] > v[j]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux

# 12
def ordenadorburbujeo(v): #
    desor = True
    while desor:
        desor = False
        for i in range(len(v)-1):
            if v[i] > v[i+1]:
                aux = v[i]
                v[i] = v[i+1]
                v[i+1] = aux
                desor = True
                
# 12.1
def ordenadorburbujeodes(v): #
    desor = True
    while desor:
        desor = False
        for i in range(len(v)-1):
            if v[i] < v[i+1]:
                aux = v[i]
                v[i] = v[i+1]
                v[i+1] = aux
                desor = True

# 13
def busquedabinaria(n,v): #
    iz = 0
    de = len(v)-1
    enc = -1
    while iz <= de and enc == -1:
        ce = (iz + de) // 2
        if v[ce] == n:
            enc = ce
        elif v[ce] > n:
            de = ce-1
        else:
            iz = ce+1
    return enc

# 14
def eliminacion_v1menosv2(v1,v2):
    for i in range(len(v2)):
        j = 0
        while j < len(v1):
            if v1[j] == v2[i]:
                del v1[j]
            j += 1


# 14.1 
def eliminaciondereps(v):
    i = 0
    deleted = []
    borrados = True
    while i < len(v)-1 and borrados:
        borrados = False
        if v[i] == v[i+1]:
            deleted.append(v[i])
            del v[i]
            borrados = True
        i += 1
    return deleted

# 15
def impresion(v): #
    for i in range(len(v)):
        print(v[i],end=' ')
    print()

# 15.1
def impresion_laterales(v,vlats):
    print('Elemento       Laterales')
    for i in range(len(vlats)):
        if vlats[i] == len(v)-1:
            lateral = v[vlats[i]-1]
        else:
            lateral = v[vlats[i]+1]
        print(v[vlats[i]],'-------------',lateral)
    
# 16
def impresioncumple(v):
    print('''  Mes        Cumpleaños
---------------------------''')
    for i in range(len(v)):
        if v[i] > 0:
            print('  ',i+1,'-----------',v[i])
    print()
    
# 16.1
def impresionmeses_max(v,n):
    print('''Meses con mas cumpleañeros:
  Mes        Cumpleaños
---------------------------''')
    for i in range(len(v)):
        if v[i] > 0:
            print('  ',v[i],'-----------',n)
    print()
    
# 17
def comp_menorigual(v):
    b = []
    for i in range(len(v)-1):
        if v[i] <= v[i+1]:
            b.append(True)
        else:
            b.append(False)
    return b

# 18
# Devuelve el tipo de ordenamiento de una lista, tipo 0 = lista desordenada, tipo 1 = lista ordenada ascendentemente
# tipo 2 lista ordenada descendentemente y tipo 3 lista con todos los elementos iguales.
def deteccion_de_orden(v):
    iz = v[0]
    de = v[len(v)-1]
    if iz < de:
        tipo = 1
        for i in range(len(v)-1):
            if v[i] > v[i+1]:
                tipo = 0
                break
    elif iz > de:
        tipo = 2
        for i in range(len(v)-1):
            if v[i] < v[i+1]:
                tipo = 0
                break        
    else:
        tipo = 3
        for i in range(len(v)-1):
            if v[i] != v[i+1]:
                tipo = 0
                break
    return tipo

# 19
def insercion_ordenada(n,v,orden):
    if orden == 1 or orden == 3:
        for i in range(len(v)):
            if i > 0 and i < len(v)-1:
                if v[i] > n and v[i-1] <= n:
                    aux = v[i]
                    v[i] = n
                    n = aux
            elif i == 0 and v[i] > n:
                aux = v[i]
                v[i] = n
                n = aux
            elif i == len(v)-1:
                if v[i] > n:
                    aux = v[i]
                    v[i] = n
                    n = aux
                v.append(n)
    else:
        for i in range(len(v)):
            if i > 0 and i < len(v)-1:
                if v[i] < n and v[i-1] >= n:
                    aux = v[i]
                    v[i] = n
                    n = aux
            elif i == 0 and v[i] < n:
                aux = v[i]
                v[i] = n
                n = aux
            elif i == len(v)-1:
                if v[i] < n:
                    aux = v[i]
                    v[i] = n
                    n = aux
                v.append(n)    
          
# 20
# recibe una lista y devuelve dos listas cargadas con: la primera con los elementos subindice par y la otra
# los elementos de subindice impar
def separacion_par_impar(v):
    vpar = []
    vimp = []
    for i in range(0,len(v),2):
        vpar.append(v[i])
    for i in range(1,len(v),2):
        vimp.append(v[i])
    return vpar, vimp

# 21 
def comparacion_laterales(v):
    vlats = []
    for i in range(len(v)):
        if i == 0:
            if v[1] == v[len(v)-1]:
                vlats.append(i)
        elif i == len(v)-1:
            if v[len(v)-2] == v[0]:
                vlats.append(i)
        else:
            if v[i-1] == v[i+1]:
                vlats.append(i)
    return vlats
        
# 22
# Debe recibir ambas listas ordenadas de manera ascendente
def intercalador(v1,v2):
    v3 = []
    i , j = 0 , 0
    while i < len(v1) or j < len(v2):
        if i == 0 and j == 0:
            if v1[i] <= v2[j]:
                v3.append(v1[i])
                i += 1
            else:
                v3.append(v2[j])
                j += 1
        else:
            if v1[i] >= v3[len(v3)-1] and v1[i] <= v2[j]:
                v3.append(v1[i])
                i += 1
            else:
                v3.append(v2[j])
                j += 1
    return v3

# 23 
def secuencias(n):
    v = []
    MI , MA = 1 , 20
    suma = 0
    for i in range(n):
        x = random.randint(MI,MA)
        suma += x
        if suma > 20:
            v.append(0)
            suma = x
        v.append(x)
    return v

# 24  
# Busqueda de la/s secuencias mas largas
def secuencia_mas_larga(v):
    sec_start = []
    longersec = 0
    for j in range(2):
        current = 0
        for i in range(len(v)):
            if v[i] != 0:
                current += 1
            else:
                current = 0
            if j == 0:
                if current > longersec:
                    longersec = current
            else:
                if current  == longersec:
                    sec_start.append(i - (longersec - 1))
    return longersec , sec_start

# 25 
# Impresion de secuencia:
def impresiondesec(v,start,length):
    for i in range(length):
        print(v[start + i],end=' ')

# ### # ### # ### # ### # ### # ### # ### # ### # ### #
# Funciones para el desarrollo del ejercicio 16, busqueda del numero
# 26.1
# Juego
def busquedadelnum(mejoresp,mejoresn,ej):
    rand = random.randint(1000,9999)
    if ej == 17:
        randlist = pasar_a_lista(rand)
    cont = 1
    guess = int(input('>Ingrese su numero: '))
    while guess != rand and guess != -1:
        if guess < 1000 or guess >9999:
            print('Numero invalido, recuerda que el numero debe estar entre 1000 y 9999, intenta de nuevo')
        else:
            cont += 1
            if ej == 16:
                if guess < rand:
                    print('Su numero es MENOR al valor secreto')
                else:
                    print('Su numero es MAYOR al valor secreto')
            else:
                pista(randlist,guess)
        print('>Intento',cont,':',end=' ')
        guess = int(input())
    if guess == -1:
        print('\n*** Partida abandonada despues de',cont-1,'intentos\n')
    else:
        cont +=1
        print('\n¡Has adivinado el valor secreto! :',rand)
        print(' Te tomo',cont-1,'intentos\n')
        mejorespunt(mejoresp,mejoresn,cont)

# 26.2
def mejorespunt(puntos,nombres,puntaje):
    if len(puntos)==1 or puntaje < puntos[1]:
        print('¡Has establecido un nuevo record!\n')
    elif puntaje == puntos[1]:
        print('¡Has igualado el mejor puntaje!\n')
    nombre = input('Ingresa tu nombre para cargarlo a la leaderboard: ')
    puntos.append(puntaje)
    nombres.append(nombre)
    ordenadorjuego(puntos,nombres)
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

def ordenadorjuego(puntos,nombres):
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

def pista(n,guess):
    guesslist = pasar_a_lista(guess)
    correcto = 0
    aprox = 0
    for i in range(4):
        if guesslist[i] == n[i]:
            correcto += 1
        elif guesslist[i] in n and guesslist[i] != n[i]:
            aprox += 1
    print(correcto,'correctos',aprox,'aproximados') 

#devuelve el numero ingresado como digistos separados en una lista  
def pasar_a_lista(n):
    v = []
    while n > 0:
        resto = n % 10
        n = n // 10
        v.append(resto)
    return v