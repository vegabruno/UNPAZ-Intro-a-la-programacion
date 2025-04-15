# 21. Escribir un programa que pida al usuario una palabra, debe mostrarla 10 veces, junto al
# número correspondiente.
# Ejemplo:
# 1 hola
# 2 hola

palabra = input("Ingrese uan palabra: ")
n = 1
while n <= 10:
  print(f'{n}: {palabra}')
  n+=1