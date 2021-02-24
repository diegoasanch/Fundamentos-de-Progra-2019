# Devolver True si el número entero recibido como primer parámetro es múltiplo
# del segundo, o False en caso contrario. Ejemplo: esmultiplo(40,8) devuelve True
# y esmultiplo(50,3) devuelve False.
def esmultiplo(a,b):
    if a%b==0:
        valor=True
    else:
        valor=False
    return valor

# programa principal
print('Vea si un numero ingresado es multiplo del segundo ingresado')
print()
A=int(input('Ingrese el primer numero: '))
B=int(input('Ingrese el segundo numreo: '))
multiplo = esmultiplo(A,B)
print(multiplo)