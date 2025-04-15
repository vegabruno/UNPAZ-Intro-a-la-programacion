nombre = input("Ingrese su nombre: ")
nombre_derecho = nombre[:]
nombre_revez = nombre[-1]+nombre[-2]+nombre[-3]+nombre[-4]+nombre[-5]

print(nombre_derecho, nombre_revez)