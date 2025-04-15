# 11. Escribir un programa que diferencie entre verdadero y falso, el usuario podrá ingresar un
# número entre 0 y 1, y el programa debe imprimir por pantalla si el número es falso o
# verdadero según lo visto en clases. Pista (True,False)

n = int(input("Ingrese 1 o 0: "))

if n == True:
    print("True")
elif n == False:
    print("False")
else:
    print("Numero incorrecto")
    
print("Fin del programa")