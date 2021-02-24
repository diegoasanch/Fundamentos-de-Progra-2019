#Leer dos números A y B enteros positivos. Calcular el producto A * B por sumas
#sucesivas e imprimir el resultado. Ejemplo: 4 * 3 = 4 + 4 + 4 (4 sumado 3 veces).
print('Ingresar dos numeros y expresar su producto como sumas sucesivas')
print()
A=int(input('Ingrese el valor de A: '))
B=int(input('Ingrese el valor de B: '))
contr=B  #contador en reversa
producto=0
while contr>0:
    contr=contr-1
    producto=producto+A
print(A,'sumado',B,'veces es',producto)