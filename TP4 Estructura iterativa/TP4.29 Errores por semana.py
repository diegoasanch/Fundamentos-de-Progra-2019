#Juancito está descontento con su rendimiento en las clases de Programación. En su primer programa
#cometió un error, en el segundo dos, en el tercero cuatro, en el cuarto ocho y así sucesivamente.
#Las clases duran S semanas y debe realizar dos programas semanales. Diseñar un programa que lea S
#y calcule el número de errores que Juancito debe esperar cometer en su último programa, si mantiene
#constante su rendimiento actual. Resolver este problema utilizando dos estrategias distintas.
print('Cuantos errores cometera Juancito en su ultimo programa??')
S=int(input('Cuantas semanas duran las clases?:'))
print()
print('Solucion 1: Elevando 2 al numero de programas por semana')
S=(2*S)-1
error=2**S
print('Juancito debe esperar cometer',error,'errores en su ultimo programa')
print()
print('Solucion 2: Elevando dos al contador hasta alcanzar S')
cont=0
while cont<=S:
    error=2**(cont)
    cont=cont+1
print('Juancito debe esperar cometer',error,'errores en su ultimo programa')