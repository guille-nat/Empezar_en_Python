from numeros import *
from os import *
import os

def equivocado():       #muestra mensaje cuando el usuario se equivoca
    print("\tPor favor ingrese una opcion valida...\n\n")
    os.system('pause')
    system("cls")
    pass


def preguntar():			#Pregunta si quiere sacar un turno 
	f =input('¿Quieres sacar otro rutno?\n'
		  '[S] <-- Sí\n'
		  '[N] <-- No\n').lower()
	system("cls")
	if f == 's':
		return False
	elif f == 'n':
		return True


def menu_principal():
	system('cls')
	op = 0
	while op != 'A':
		op = input('\tPor favor elija turno a sacar: \n'
					'\t*------------------------------*\n'
					'\t|    [P] <-- Perfumerian       |\n'
					'\t|    [F] <-- Farmacian         |\n'
					'\t|    [C] <-- Cosmeticonn       |\n' 
					'\t*------------------------------*\n'
					'\t               [A] <-- APAGAR\n'
					'\nIngrese: ').upper()
		system("cls")
		if op == 'P':
			print(next(perf))
			system('pause')
			system("cls")
			x = preguntar()
			if x == True:
				break
			elif x == False:
				pass

		elif op == 'F':
			print(next(farm))
			system('pause')
			system("cls")
			x = preguntar()
			if x == True:
				break
			elif x == False:
				pass
		elif op == 'C':
			print(next(cosm))
			system('pause')
			system("cls")
			x = preguntar()
			if x == True:
				break
			elif x == False:
				pass
		elif op == 'A':
			x = input('¿Desea apagar el sistema?\n'
				'[S] <-- Sí\n'
				'[N] <-- No\n').lower
			if x == 's':
				break
			elif x == 'n':
				pass
		else:
			equivocado()
	print('Apagando...')

menu_principal()

