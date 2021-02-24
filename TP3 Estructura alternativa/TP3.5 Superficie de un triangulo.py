#Desarrollar un programa para leer la base y la altura de un triángulo e imprimir
# su superficie. El algoritmo debe validar los datos de entrada, verificando que
# éstos sean números positivos. En caso contrario debe imprimirse el dato erróneo
# junto con una leyenda aclaratoria. Se recuerda que Sup = (Base * Altura) / 2.
print()
print('Calculador de Superficie de un Triangulo')
print()

base=float(input('Ingrese la base del triangulo: '))
altura=float(input('Ingrese la altura del triangulo: '))
sup=(base*altura)/2
print()
if base>0 and altura>0:
    print('Su triangulo tiene el valor',"{0:.2f}".format(sup),'de superficie')
elif base<0 or altura<0:
    print('Superficie:',"{0:.2f}".format(sup))
    print('**!Este calculo es erroneo debido al ingreso negativo de uno o ambos parametros!**')
else:
    print("{0:.2f}".format(sup),'Ingrese un numero mayor a cero en ambos parametros!')
