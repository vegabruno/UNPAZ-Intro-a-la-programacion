# 23. Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la
# cuenta atrás desde ese número hasta cero separados por comas. (Investigue cómo mostrar
# datos con print en la misma línea de texto), Si se anima trate de no imprimir la última coma
# después del 0.
# Ejemplo: 5
# Esta bien
# 5,4,3,2,1,0,
# Está mejor...
# 5,4,3,2,1,0

# n = int(input("Ingrese un numero positivo: "))

# while n >= 0:
#   print(f'{n}')
#   n-=1

numero = int(input("Ingresá un número entero positivo: "))

if numero > 0:
  while numero > 0:
      print(numero, end=",") #end= indica que se pone al final del menaje en consola
      numero -= 1            #Por defecto, es end="\n", al cambiarlo por "," no se dara el salto

  # Imprimir el 0 sin coma al final
  print(0)
else:
  print("Numero no permitido, ingrese un numero entero positivo.")