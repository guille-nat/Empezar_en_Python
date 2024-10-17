def Turno_Perfumeria():
	num = 0
	while True:
		num += 1
		texto = f'Su turno es el:\n \tP-{"%02d"%num} \nAguarde y sera Atendido...\n'
		yield texto

def Turno_Farmacia():
	num = 0
	while True:
		num += 1
		texto = f'Su turno es el:\n \tF-{"%02d"%num} \nAguarde y sera Atendido...\n'
		yield texto
def Turno_Cosmetico():
	num = 0
	while True:
		num += 1
		texto = f'Su turno es el:\n \tC-{"%02d"%num} \nAguarde y sera Atendido...\n'
		yield texto

perf = Turno_Perfumeria()
farm = Turno_Farmacia()
cosm = Turno_Cosmetico()

