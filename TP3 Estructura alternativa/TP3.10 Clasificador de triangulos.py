#Desarrollar un programa para leer las longitudes de los tres lados de un triángulo
# L1, L2, L3 y determinar qué tipo de triángulo es según la siguiente clasificación:
# · Si A >= B + C no se trata de un triángulo.
# · Si A² = B² + C² se trata de un triángulo rectángulo.
# · Si A² > B² + C² se trata de un triángulo obtusángulo.
# · Si A² < B² + C² se trata de un triángulo acutángulo.
# Tener en cuenta que A denota el mayor de los lados L1, L2 y L3, mientras que B
# y C corresponden a los dos lados restantes.
op=1
print()
print('Clasificador de triangulos')
while op==1:
    print()
    L1=float(input('Ingrese el primer lado del triangulo: '))
    L2=float(input('Ingrese el segundo lado del triangulo: '))
    L3=float(input('Ingrese el tercer lado del triangulo: '))
    if L1>L2 and L1>L3:
        A=L1
        B=L2
        C=L3
    elif L1<L2 and L2>L3:
        A=L2
        B=L1
        C=L3
    else: #L1<L3and L2<L3:
        A=L3
        B=L1
        C=L2
    print()
    print('El lado A=',A,'el lado B=',B,'y el lado C=',C)
    print()
    if A>=B+C:
        print('Los datos ingresados no coinciden con un triangulo :(')
    elif A**2==B**2+C**2:
        print('El triangulo ingresado es uno Rectangulo')
    elif A**2>B**2+C**2:
        print('Es un triangulo Obtusangulo')
    else:
        print('Es un triangulo acutangulo')
    op=int(input('1 O 0?:'))
while op==0:
    print('Adios')
    op=2
