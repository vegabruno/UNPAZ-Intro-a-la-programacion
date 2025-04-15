# 16.
# Escribir un programa que permita realizar 3 cálculos aritméticos, suma, resta y multiplicación.
# Las opciones deben presentarse a modo de menú de opciones , el usuario elegirá la
# operación deseada , el programa deberá verificar si el valor ingresado está entre las
# opciones del menú , si la opción ingresada no es correcta debe mostrar un mensaje que diga
# opción incorrecta y salir del programa pero si la opción es correcta seguirá con el programa y
# se le pedirá al usuario el ingreso de dos números enteros para ejecutar la operación
# seleccionada, luego debe mostrar la operación seleccionada, el desarrollo y el resultado.
# ejemplo :
# Menú:
# Suma (1) Resta (2) Multiplicación (3)
# opción: 1
# dato : 1
# dato : 2
# El resultado de la suma 1 + 2 = 3

opcion = int(input(f'''
Menú:
Suma (1) Resta (2) Multiplicación (3)
opción: '''))

n1 = int(input("Ingrese el 1er numero: "))
n2 = int(input("Ingrese el 2do numero: "))

if opcion == 1:
  print(f'El resultado de la suma: {n1 + n2}')
elif opcion == 2:
  print(f'El resultado de la resta: {n1 - n2}')
elif opcion == 3:
  print(f'El resultado de la multiplicacion: {n1 * n2}')
else:
  print("Opcion incorrecta")

print("\nFin del programa")