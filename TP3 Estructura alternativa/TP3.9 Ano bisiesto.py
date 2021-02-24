#Leer un número correspondiente a un año e imprimir un mensaje indicando si es bisiesto
# o no. Se recuerda que un año es bisiesto cuando es divisible por 4. Sin embargo, aquellos
# años que sean divisibles por 4 y también por 100 no son bisiestos, a menos que también
# sean divisibles por 400. Por ejemplo, 1900 no fue bisiesto pero sí el 2000.
print()
print('Calcula si un año es bisiesto')
print()
yr=int(input('Ingresa el año: '))
bis4=yr%4
bis100=yr%100
bis400=yr%400
print()
if bis4==0:
    if bis100==0 and bis400!=0:
        print('El año',yr,'no es bisiesto')
    else:
        print('El año',yr,'es bisiesto')
else:
    print('El año',yr,'no es bisiesto')
print()
print(':)')
