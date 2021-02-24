#Un banco necesita para sus cajeros automáticos un programa que lea
#una cantidad de dinero e imprima a cuántos billetes equivale, considerando
#que existen billetes de $100, $50, $10, $5 y $1. Desarrollar dicho programa
#de tal forma que se minimice la cantidad de billetes entregados por el cajero.
print('Cajero Automatico')
print()
monto=float(input('Ingrese el monto a extraer: '))
print()

b100=monto//100
resto100=monto%100

b50=resto100//50
resto50=resto100%50

b10=resto50//10
resto10=resto50%10

b5=resto10//5
resto5=resto10%5

b1=resto5//1
resto1=resto5%1

# No pedido en el programa, pero anadido porque YOLO
c50=resto1//0.50
restoc50=resto1%0.50

c25=restoc50//0.25
restoc25=resto50%0.25

c10=restoc25//0.10
restoc10=restoc25%0.10

c5=restoc10//0.05
restoc5=restoc10%0.05

c1=restoc5//0.01
centavos=c50+c25+c10+c5+c1

total1=b100*100+b50*50+b10*10+b5*5+b1
total2=b100*100+b50*50+b10*10+b5*5+b1+c50*0.5+c25*0.25+c10*0.1+c5*0.05+c1*0.01

if(centavos==0):
    print('Su monto a retirar de',"{0:.0f}".format(monto),'pesos, lo obtendra en:')
    print()
    print('Billetes de 100:      ',"{0:.0f}".format(b100))
    print('Billetes de 50:        ',"{0:.0f}".format(b50))
    print('Billetes de 10:        ',"{0:.0f}".format(b10))
    print('Billetes de 5:          ',"{0:.0f}".format(b5))
    print('Billetes de 1:          ',"{0:.0f}".format(b1))
    print('.........................................')
    print('Total:           $         ',"{0:.2f}".format(total1))
else:
    print('Su monto a retirar de',monto,'pesos, lo obtendra en:')
    print()
    print('Billetes de 100:      ',"{0:.0f}".format(b100))
    print('Billetes de 50:        ',"{0:.0f}".format(b50))
    print('Billetes de 10:        ',"{0:.0f}".format(b10))
    print('Billetes de 5:          ',"{0:.0f}".format(b5))
    print('Billetes de 1:          ',"{0:.0f}".format(b1))
    print('Monedas de 50c   ',"{0:.0f}".format(c50))
    print('Monedas de 25c   ',"{0:.0f}".format(c25))
    print('Monedas de 10c   ',"{0:.0f}".format(c10))
    print('Monedas de 5c     ',"{0:.0f}".format(c5))
    print('Monedas de 1c     ',"{0:.0f}".format(c1))
    print('.........................................')
    print('Total:           $         ',"{0:.2f}".format(total2))
