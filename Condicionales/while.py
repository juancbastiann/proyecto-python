#EJEMPLO 1
numero = 10
suma = 10

while numero <= 10:
    suma = numero + suma
    numero = numero + 1
print ("La suma es " + str(suma))

#EJEMPLO 2
num = 2

while num < 9 or num > 19:
    num = int(input('ingresar numero positivo: '))

print('.....')

#EJEMPLO 3
num = 2

if num >= 10 and num <= 20 and num%2 == 0:
    pass

while not(num >= 10 and num <= 20 and num%2 == 0):
    num = int(input('ingresar números positivos: '))

print('.....')