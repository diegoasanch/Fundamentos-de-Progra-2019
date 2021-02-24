def listado():
    print('''
   Ejercicios:
1 - Ingresar numeros entre 1 y 20 a una lista
2 - Calcular la suma de los elementos de una lista
3 - Determinar si una lista es capicua
4 - Invertir valores en posicion impar de una lista
5 - Busqueda secuencial en lista desordenada
6 - Busqueda binaria en lista ordenada
7 - Cumpleaños en una escuela
8 - Lista con numeros al azar entre 0 y 100, busqueda maximo y minimo
9 - Comparacion de valores consecutivos en una lista
10 - Cargar 2 listas y realiza 3 operaciones
11 - Agregar un numero a una lista manteniendo el orden
12 - Lee una lista y realiza 3 operaciones
13 - Detecta el tipo de ordenamiento (o falta de el) en una lista
14 - Elimina de una lista los elementos pertenecintes a otra
15 - Intercala dos listas ordenadas manteniendo el orden sin usar ordenador
16 - Juego busqueda del numero
17 - Juego busqueda del numero con pista de numeros
18 - Secuencia de numeros al azar separado en segmentos de 20
19 - Ejercicio anterior, muestra secuencia mas larga
   --- Ingrese (-1) para salir del programa ---
''')
    
def ej1():
    print('''
Escribir una función para ingresar desde el teclado una serie de números entre 1 y 20
y guardarlos en una lista. En caso de ingresar un valor fuera de rango el programa
mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la carga se
deberá ingresar -1. La función no recibe ningún parámetro, y devuelve la lista cargada
(o vacía, si el usuario no ingresó nada) como valor de retorno.
''')
    
def ej2():
    print('''
Calcular la suma de los números de una lista (usando la carga de lista del ej1)
''')
    
def ej3():
    print('''
Determinar si una lista es capicúa. (usando la carga de lista del ej1)
''')
    
def ej4():
    print('''
Invertir aquellos valores ubicados en posiciones impares de una lista.
(usando la carga de lista del ej1)
''')
    
def ej5():
    print('''
Escribir una función para devolver la posición que ocupa un valor pasado como
parámetro, utilizando búsqueda secuencial en una lista desordenada. La función
debe devolver -1 si el elemento no se encuentra en la lista. (usando la carga 
de lista del ej1)
''')
    
def ej6():
    print('''
Cargar y ordenar una lista, luego ingresar un numero para buscar su posion dentro
de la lista mediante el metodo de busqueda binaria
''')
    
def ej7():
    print('''
Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del
año, con el propósito de ofrecerles un agasajo especial en su día. Desarrollar un
programa que lea el número de legajo y fecha de nacimiento (día, mes y año) de
cada uno de los alumnos que concurren a dicha escuela. La carga finaliza con un
número de legajo igual a -1. Emitir un informe donde aparezca -mes por mes cuántos 
alumnos cumplen años a lo largo del año. Imprimir también una leyenda
que indique cuál es el mes con mayor cantidad de cumpleaños.
''')
    
def ej8():
    print('''
Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir 
el valor mínimo y el lugar que ocupa. Tener en cuenta que el mínimo puede
estar repetido, en cuyo caso deberán mostrarse todas las posiciones que ocupe.
La carga de datos termina cuando se obtenga un 0 como número al azar, el que
no deberá cargarse en la lista.
''')
    
def ej9():
    print('''
Dado una lista de N números (por ejemplo 5), devolver una lista de N-1 valores
booleanos, tal que cada valor de este último arreglo corresponde al resultado de
la comparación de los pares de valores consecutivos del primer arreglo. El valor
booleano es True si el primer elemento del par es menor o igual que el siguiente,
y False si no lo es.
''')
    
def ej10():
    print('''
Cargar dos listas de números A y B. Se solicita construir e imprimir tres nuevas
listas C, D y E que contengan:
· La concatenación de los valores pares de A con los impares de B.*
· La concatenación de los valores pares de A con el reverso de los valores
   pares de B. ("valores pares" o "valores impares" se refiere a los elementos
   propiamente dichos y no a sus posiciones).
· La intercalación de los elementos de A y B.
''')
    
def ej11():
    print('''
Dada una lista ordenada de números llamada A y un nuevo número N, desarrollar
un programa que agregue el elemento N dentro de la lista A, respetando el
ordenamiento existente. El programa deberá detectar automáticamente si el 
ordenamiento es ascendente o descendente antes de realizar la inserción.
''')
    
def ej12():
    print('''
Leer una lista de números V. Luego se solicita:
· Calcular el producto de los elementos de subíndice par y dividirlo por la
  suma de los elementos de subíndice impar, sólo si esta suma es distinta
  de cero. Imprimir la lista leída y el resultado calculado, o un mensaje de
  error en caso de no poder realizar la operación.
· Generar e imprimir otra lista tal que su primer elemento contenga la
  suma del primero más el último elemento de la lista V; el segundo elemento
  contenga la suma del segundo más el penúltimo de V, etc. La
  nueva lista contendrá la mitad de los elementos de la lista original.
· Imprimir un listado de aquellos elementos de V que cumplan con la condición de
  tener iguales sus dos elementos laterales (el anterior y el siguiente). Si 
  ninguno cumple esta condición, se imprimirá una leyenda
  aclaratoria. Considerar que los extremos de la lista se encuentran unidos,
  de modo que el último elemento se encuentra antes que el primero, y que el
  primer elemento se encuentra después del último
''')
    
def ej13():
    print('''
Realizar un programa que permita ingresar números en una lista, finalizando la
lectura con -1. Informar si la secuencia de elementos ingresada es ascendente,
descendente, todos sus valores son iguales o se encuentra desordenada.
''')
    
def ej14():
    print('''
Eliminar de una lista de números enteros los valores que se encuentren en una
segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante.
''')
    
def ej15():
    print('''
Leer dos listas de números M y N, ambas ordenadas de menor a mayor. Generar
e imprimir una tercera lista que resulte de intercalar los elementos de M y N. La
nueva lista también debe quedar ordenada, sin utilizar ningún método de ordenamiento.
''')
    
def ej16():
    print('''
Desarrollar un programa que genere un número entero al azar de cuatro cifras y
proponerle al usuario que lo descubra, ingresando valores repetidamente hasta
hallarlo. En cada intento el programa mostrará mensajes indicando si el número
ingresado es mayor o menor que el valor secreto. Permitir que el usuario abandone
al ingresar -1. Informar la cantidad de intentos realizada al terminar el juego,
haciendo que el usuario ingrese su nombre si mejoró la mejor marca de intentos 
obtenida hasta el momento. Luego mostrar la lista de los 5 mejores puntajes y 
preguntar si se desea jugar otra vez, reiniciando el juego en caso afirmativo.
''')

def ej16_instrucciones():
  print('''
  instrucciones
+----------+----------+----------+----------+----------+----------+----------+----------+----------+
             El juego consiste en adivinar un numero al azar generado por la computadora
  Las opciones posibles estan entre el 1000 y el 9999, si tu numero ingresado no es el valor secreto
   el programa te informara si estas adivinando un numero mayor o menor para que adivines de nuevo.
          Si deseas abandonar la partida sin terminarla ingresa el numero -1. ¡Buena suerte!
+----------+----------+----------+----------+----------+----------+----------+----------+----------+
''')
    
def ej17():
    print('''
Modificar el programa anterior para que las pistas brindadas por el programa no
sean del tipo "es mayor" o "es menor" sino "M dígitos correctos y N dígitos
aproximados". Se considera que un dígito es correcto cuando tanto su valor
como su posición coinciden con los del número secreto, mientras que un dígito
es aproximado cuando coincide el valor pero no su posición. Ejemplos:
Número secreto: 5739
· Intento 1: 1234 -> 1 correcto
· Intento 2: 5678 -> 1 correcto y 1 aproximado
· Intento 3: 9375 -> 4 aproximados
''')

def ej17_instrucciones():
      print('''
  instrucciones
+----------+----------+----------+----------+----------+----------+----------+----------+----------+
             El juego consiste en adivinar un numero al azar generado por la computadora
  Las opciones posibles estan entre el 1000 y el 9999, si tu numero ingresado no es el valor secreto
   el programa te informara cuantos digitos tienes correctos (valor y posicion correctos) y cuantos.
                 digitos tienes aproximados (valor correcto pero posicion diferente)
          Si deseas abandonar la partida sin terminarla ingresa el numero -1. ¡Buena suerte!
+----------+----------+----------+----------+----------+----------+----------+----------+----------+
''')
def ej18():
    print('''
Ingresar por teclado un número N y construir una lista llamada SECUENCIAS con
N números enteros al azar entre 1 y 20. Esta lista se caracterizará porque sus
valores deben encontrarse divididos en secuencias de números separadas por
ceros, cuya suma no sea mayor que 20. Para eso se deberá agregar un elemento
de valor 0 a fin de separar cada secuencia de la siguiente, cuidando que ninguna
secuencia sume más de 20. Agregar un 0 adicional al final de la lista y mostrar la
lista obtenida por pantalla
''')
    
def ej19():
    print('''
A partir de la lista SECUENCIAS generada en el ejercicio anterior, imprimir la
secuencia más larga almacenada en la misma. Si hubiera varias secuencias con
la misma longitud máxima deberán mostrarse todas las que correspondan.
''')