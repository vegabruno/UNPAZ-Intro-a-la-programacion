# 15. Escriba un programa que pida dos números y que muestre cuál es el menor y cuál el mayor o
# que muestre si son iguales.

n1 = int(input("Ingrese el 1er numero: "))
n2 = int(input("Ingrese el 2do numero: "))

if n1 > n2:
  print(f'El numero {n1} es mayor que {n2}')
elif n2 > n1:
  print(f'El numero {n2} es mayor que {n1}')
else:
  print("Los numeros son iguales")