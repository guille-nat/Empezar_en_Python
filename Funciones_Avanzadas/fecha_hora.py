import datetime


mi_hora = datetime.time(00,18,35)
mi_dia = datetime.date(2023,7,22)

print(mi_dia)
print(mi_hora)
#print(mi_dia.ctime())	#<--- lo muestra con otro formato
#print(mi_dia.today())	#<-- muestra el dia de hoy de la fecha

#mi_fecha = datetime(2023,7,22,00,18,35) # <--- date y time junto

#mi_fecha = mi_fecha.replace( year = 2027) #<-- para cambiar la fecha 

#print(mi_fecha)

#----------------------- CALCULAR TIEMPOS -----------------#
'''
from datetime import datetime

nacimiento = date(1987,5,23)
defuncion = date(2050,9,12)
vida = defuncion - nacimiento #cuantos dias vivio	
print(vida) '''

#despierta = datetime(2022,12,15,1,30)
#durmio = datetime(2022,12,14,20,16)

#tiempo = despierta-durmio

#print(tiempo)