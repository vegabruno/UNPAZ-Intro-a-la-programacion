# 17. Escribir un programa que nos muestre si es hora de desayunar, almorzar, merendar o cenar
# dependiendo de la hora ingresada, según el siguiente listado.
# 10 Desayuno
# 13 Almuerzo
# 17 Merienda
# 21 cena

hora = int(input("Ingrese que hora es: "))

match hora:
  case 10:
    print("Hora de desayunar")
  case 13:
    print("Hora de almorzar")
  case 17:
    print("Hora de merendar")
  case 21:
    print("Hora de cenar")
  case _:
    print("No es hora de comer")
# if hora ==10:
#   print("Hora de desayunar")
# elif hora ==13:
#   print("Hora de almorzar")
# elif hora ==17:
#   print("Hora de merendar")
# elif hora ==21:
#   print("Hora de cenar")
# else:
#   print("No es la hora de comer")