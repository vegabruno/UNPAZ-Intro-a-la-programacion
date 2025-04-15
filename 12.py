# 12. Escribir un programa permita el ingreso de una letra, el programa debe mostrar un aviso si la
# letra es vocal o consonante.

letra = input("Ingrese una letra: ").upper()

match letra:
    case "A":
        print(f"{letra}: Vocal")
    case "E":
        print(f"{letra}: Vocal")
    case "I":
        print(f"{letra}: Vocal")
    case "O":
        print(f"{letra}: Vocal")
    case "U":
        print(f"{letra}: Vocal")
    case _:
        print(f"{letra}: Consonante")