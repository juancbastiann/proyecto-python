#EJEMPLO 1
j = 0
for i in range(10):
    j += 2
    print('i:', i, 'j:', j)
    if j >= 2 and j <= 18:
        continue
    print('el valor de j:', j)

#EJEMPLO 2
x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)

#EJEMPLO 3
semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
findesemana = ['Sábado', 'Domingo']

for day in semana:

    if day in findesemana:
        print(f'Hoy {day} no se trabaja')
        continue

    print(f'Hoy {day} toca trabajar')