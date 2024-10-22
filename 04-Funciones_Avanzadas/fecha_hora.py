import datetime

# Crear un objeto de tiempo
mi_hora = datetime.time(00, 18, 35)
print(f'Hora: {mi_hora}')
# Crear un objeto de fecha
mi_dia = datetime.date(2023, 7, 22)
print(f'Fecha: {mi_dia}')

# print(mi_dia.ctime())	#<--- lo muestra con otro formato
# print(mi_dia.today())	#<-- muestra el dia de hoy de la fecha

mi_fecha = datetime(2023, 7, 22, 00, 18, 35)  # <--- date y time junto
print(mi_fecha)

mi_fecha = mi_fecha.replace(year=2027)  # <-- para cambiar la fecha
print(mi_fecha)

# ----------------------- CALCULAR TIEMPOS -----------------#

# Calcular la diferencia entre dos fechas
nacimiento = datetime.date(1987, 5, 23)
defuncion = datetime.date(2050, 9, 12)
vida = defuncion - nacimiento
print(f'Días vividos: {vida.days}')


# Calcular la diferencia entre dos fechas
nacimiento = datetime.date(1987, 5, 23)
defuncion = datetime.date(2050, 9, 12)
vida = defuncion - nacimiento
print(f'Días vividos: {vida.days}')
