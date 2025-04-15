# 10. Escribir un programa que permita que permita ingresar su año de nacimiento sin decimales,
# y calcular SI ya pasaron 18 años, si ya pasaron 18 años, mostrar cuantos años pasaron
# desde que cumplio los 18 años junto al mensaje que diga: “Ud es mayor de edad hace: .......
# años, porque este año usted tendrá .... años". Indique la finalización del programa

año = int(input("Ingrese su año de nacimiento: "))

edad = 2025 - año

if edad >= 18:
    print(f'Ud es mayor de edad hace: {edad-18} años, porque este año usted {edad} años')

print("Fin del programa")