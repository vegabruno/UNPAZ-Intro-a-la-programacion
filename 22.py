# 22. Escribir un programa que pregunte al usuario cuantos años cumplio o cumplira este año
# a. Debe calcular el año de nacimiento , teniendo en cuenta el año actual.
# b. Debe mostrar por pantalla el año de nacimiento y los años que ha cumplido cada
# año hasta la edad actual.
# Ejemplo: 5
# 2017 0 años
# 2018 1 años
# 2019 2 años
# 2020 3 años
# 2021 4 años
# 2022 5 años

edad = int(input("Ingrese cuantos años cumplira este 2025: "))
edad_por_anio = 0
nacimiento = 2025 - edad

while edad_por_anio <= edad:
  print(f'{nacimiento} {edad_por_anio}')
  edad_por_anio += 1
  nacimiento +=1
