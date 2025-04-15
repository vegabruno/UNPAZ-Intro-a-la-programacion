'''Escribir un programa que permita que permita ingresar una nota numérica entre 1 y
10,(utilizar 3 condicionales simples)
Condiciones Mensajes por pantalla
Si la nota está entre 1 y 3 desaprobó
Si la nota está entre 4 y 6 aprobó .
Si la nota es 7 o más promociono'''

nota = int(input("Ingrese su nota: "))

if nota >=1 and nota <=3:
    print(f'''Nota {nota}: Desaprobó''')

if nota >=4 and nota <=6:
    print(f'''Nota {nota}: Aprobó''')
    
if nota >=7 and nota <=10:
    print(f'''Nota {nota}: Promocionó''')

if nota < 1 or nota > 10:
    print(f'''Nota {nota}: No valida, intente nuevamente''')