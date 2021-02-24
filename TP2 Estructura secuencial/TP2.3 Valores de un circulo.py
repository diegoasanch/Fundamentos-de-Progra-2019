#Ingresar la longitud del radio de un círculo. Calcular e imprimir:
#· La superficie del círculo (Sup = p * r²)
#· El perímetro de la circunferencia (Per = p * d)
#· La superficie de la esfera (Sup = 4 * p * r²)
#· El volumen de la esfera (Vol = 4/3 * p * r³)
print('Calculador de los valores de un circulo en funcion a su radio')
print()
r=float(input('Ingresa la longitud del radio del circulo: '))
d=r*2
pi=3.1416
supC=pi*r**2
perC=pi*d
supE=4*pi*r**2
volE=4/3*pi*r**3
print()
print('Nuestro circulo con radio=',r,'tiene como valores:')
print()
print('La superficie del circulo es',supC)
print('El perimetro de la circunferencia es',perC)
print('La superficie de la esfera es',supE)
print('El volumen de la esfera es',volE)

