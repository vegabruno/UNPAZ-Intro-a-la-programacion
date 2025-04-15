# 14. Escribir un programa que permita calcular la suma de tres números enteros ingresados por
# teclado. Si el resultado es mayor a 50 dividir por 2 , En caso contrario elevar el resultado al
# cubo, si al calcular el cubo el resultado es superior a 5000 deberá mostrar por pantalla “Este
# es un gran número”

n1 = int(input("Ingrese el 1er numero: "))  
n2 = int(input("Ingrese el 2do numero: "))
n3 = int(input("Ingrese el 3er numero: "))

resultado = n1+n2+n3
if resultado > 50:
  resultado/2
else:
  resultado**3
  if resultado > 5000:
    print("Este numero es un gran numero.")
    
print(f'Suma total: {resultado}')