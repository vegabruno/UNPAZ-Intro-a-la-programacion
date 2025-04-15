# 26. Escribir un programa que muestre un menú con las siguientes opciones:
# a. Suma.
# b. Multiplicación
# c. Largo de Palabras
# d. Salir
# Funcionamiento:
# ● El usuario debe ver el menú de opciones todo el tiempo.
# ● Si elige la opción a
# debe solicitar 2 números, sumarlos y mostrarlos.
# Si elige la opción b
# debe solicitar 2 números, multiplicarlos y mostrarlos.
# ● Si elige la opción c,
# Debe solicitar dos palabras y mostrar la palabra más larga, avisar cuando
# sean iguales.en ambos casos debe mostrar el largo de cada una
# ● Si elige la opción d
# Debe salir y despedir al usuario.



while True:
  opcion = input(f'''
    a. Suma.
    b. Multiplicación
    c. Largo de Palabras
    d. Salir
    ''').lower()
  
  match opcion:
    case "a":
      n1 = int(input("Ingrese el 1er numero entero: "))
      n2 = int(input("Ingrese el 2do numero entero: "))
    
      print(n1 + n2)
    case "b":
      n1 = int(input("Ingrese el 1er numero entero: "))
      n2 = int(input("Ingrese el 2do numero entero: "))
      
      print(n1*n2)
    case "c":
      str1 = input("Ingrese la 1er palabra: ")
      str2 = input("Ingrese la 2da palabra: ")
      str1_len = len(str1)
      str2_len = len(str2)
      if str1_len > str2_len:
        print(f'{str1} ({str1_len}) es mas larga que {str2} ({str2_len})')
      elif str1_len < str2_len:
        print(f'{str2} ({str2_len}) es mas larga que {str1} ({str1_len})')
      else:
        print(f'{str1} y {str2} miden {str1_len} caracteres.')
    case "d":
      print("Gracias por usar el programa! Saliendo... ")
      break