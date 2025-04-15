# 13. Escribir un programa que ayude a escoger un destino para irse de vacaciones, entonces, el
# usuario ingresa por teclado el mes que se tomara las vacaciones (en formato numérico ), si
# ingresa el mes diciembre, enero, febrero o marzo, mostraremos por pantalla por siguientes
# puntos turísticos “Mar del plata”, “Santa Teresita”, “Córdoba”, “San luis”, pero si elije los
# meses junio, julio o agosto mostraremos por pantalla "Cataratas", "Bariloche","Perito
# Moreno", si elige cualquier otro mes mostraremos por pantalla "No tenemos sugerencias
# cargadas." , los sitios turísticos se deben mostrar uno debajo de otro.
# mes: 12
# Mar del plata
# Santa Teresita
# ....

mes = int(input("Ingrese el mes que se irá de vacaciones: "))
enero = 1
febrero = 2
marzo = 3
if mes == 12 or (mes >= 1 and mes <=3):
    print(f'''
Mes: {mes}
Mar del plata
Santa teresita
Cordoba
San Luis
''')
elif (mes >= 6 and mes <=8):
    print(f'''
Mes: {mes}
Cataratas
Bariloche
Perito Moreno
''')
else:
    print("Lo sentimos, no tenemos sugerencias cargadas.")