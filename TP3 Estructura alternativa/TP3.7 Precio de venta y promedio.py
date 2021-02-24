#Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
#· Aplica el precio base a la primera docena de unidades.
#· Aplica un 10% de descuento a todas las unidades entre 13 y 100.
#· Aplica un 25% de descuento a todas las unidades por encima de las 100.
# Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio
# base es 100. El cálculo resultante sería:
# 100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04
# Desarrollar un programa que lea la cantidad solicitada de un producto y su precio base,
# e imprima el valor total de la venta y el precio promedio.
print()
print('TreeShop')
print()

base=float(input('Ingrese el precio base del producto: '))
cant=int(input('Ingrese la cantidad de producto: '))
print()

if cant>0 and cant<=12:
    total=base*cant
    print('Articulo        $',base)
    print('Cantidad     ',cant)
    print('........................................')
    print('Total              $',"{0:.2f}".format(total))
    
elif cant>12 and cant<=100:
    total=base*12+(base*(cant-12))*0.9
    prom=total/cant
    print('Articulo        $',base)
    print('Cantidad     ',cant)
    print('........................................')
    print('Total              $',"{0:.2f}".format(total))
    print('Promedio     $',"{0:.2f}".format(prom))
    
elif cant>100:
    total=base*12+(base*88)*0.9+(base*(cant-100))*0.75
    prom=total/cant
    print('Articulo        $',base)
    print('Cantidad     ',cant)
    print('........................................')
    print('Total              $',"{0:.2f}".format(total))
    print('Promedio     $',"{0:.2f}".format(prom))
else:
    print('***INGRESE UNA CANTIDAD VALIDA***')
