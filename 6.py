'''Escribir un programa que permita el ingreso por teclado de una oración de cinco palabras, y
muestras por pantalla, en minúsculas, en mayúsculas y por último solo el primer caracter de
la oración en mayúscula.'''
texto = input("Ingrese la oración: ")

print(f'''
{texto.capitalize()}
{texto.lower()}
{texto.upper()}
''')