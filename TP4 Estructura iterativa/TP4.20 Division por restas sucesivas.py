#Leer A y B enteros positivos y verificar que A >= B. Una vez hecha esta verificación, dividir A sobre B mediante restas
#sucesivas, es decir sin utilizar el operador
#de división. Ejemplo 5 dividido 2:
#· Restamos el dividendo menos el divisor: 5 - 2 = 3
#· Repetimos esta resta tantas veces como sea posible: 3 - 2 = 1
#· Al ser el resultado (1) menor que el divisor (2), detenemos el proceso.
#· Este resultado es el resto de la división, mientras que el cociente se
#obtiene contando la cantidad de restas que se efectuaron. Imprimir dividendo, divisor, cociente y resto.
print('Division mediante restas sucesivas')
print()
A=int(input('Ingrese el valor de A: '))
B=int(input('Ingrese el valor de B: '))
cociente=0
if A>=B:
    divisor=A
    while divisor>=B:
        divisor=divisor-B
        cociente=cociente+1
    resto=divisor
    print()
    print('Divisor=',A,'Dividendo=',B)
    print('Cociente=',cociente,'Resto=',resto)
else:
    print('No se puede realizar la division',A,'entre',B)