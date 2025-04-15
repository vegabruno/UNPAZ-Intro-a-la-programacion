# 27. Escribir un programa que solicite una frase al usuario y luego una letra, usando while y lo
# aprendido sobre string en las clases anteriores, acceso a cada caracter de una cadena por
# medio del elemento palabra[0], (no use IN).
# Buscar si la letra que ingresó se encuentra en la frase solicitada.
# Cuente cuántas veces está esa letra dentro de la frase
# Si, esta mostrará un mensaje que diga “letra ... encontrada aparece ... veces.
# Si no está mostrara “Letra ... no encontrada en la frase”
# Luego de resolver debe preguntar al usuario si quiere salir debe ingresar una letra “S” o si
# presiona cualquier otra letra continuará.


while True:
  frase = input("Ingrese una frase: ").lower()
  letra = input("Ingrese la letra: ").lower()
  cant_letra = 0
  i = 0
  while i < len(frase):
    if frase[i] == letra:
      cant_letra += 1
    i+=1
    
  if cant_letra > 0:
    print(f'letra {letra} encontrada, aparece {cant_letra} veces')
    cant_letra = 0
    i = 0
  else:
    print(f'Letra {letra} no encontrada en la frase')
    i = 0
    
  salir = input("Presione 'S' para salir o cualquier tecla para continuar: ").lower()
  if salir == "s":
    break