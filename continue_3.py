semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
findesemana = ['Sábado', 'Domingo']

for day in semana:

    if day in findesemana:
        print(f'Hoy {day} no se trabaja')
        continue

    print(f'Hoy {day} toca trabajar')