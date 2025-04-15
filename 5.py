'''Escribir un programa que solicite la fecha de nacimiento en formato “dd/mm/aaaa” , y
muestre por pantalla la fecha por separado el día,el mes y el año.
Ejemplo: El usuario ingresa “23/08/2022” el programa debe mostrar:“ Día:23 - Mes:08 -
Año:2022 ”.
'''

dia = (input('Ingrese su fecha de nacimiento en formato dd/mm/aaaa: '))

print(f'''
Dia: {dia[:2]}
Mes: {dia[3:5]}
Año: {dia[6:]}
''')