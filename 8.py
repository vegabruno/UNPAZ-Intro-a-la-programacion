'''Escribir un programa que permita el ingreso de 2 digitos, si es menor a 20 debe mostrar la
mitad de ese número.'''

digitos = int(input('Ingrese 2 digitos: '))

if digitos < 20 and digitos >= 10:
    print(digitos/2)
else:
    print("Error: ingrese 2 digitos")