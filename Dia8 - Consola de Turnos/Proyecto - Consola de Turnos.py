import numeros2

def preguntar():
    print("Bienvenido a la consola de turnos")
    while True:
        print ("[P] Perfumería'\n[F] Farmacia'\n[C] Cosmética")
        try:
            rubro = input("Ingrese la letra de su rubro: ").upper()
            if rubro not in "PFC":
                raise ValueError
        except ValueError:
            print("Rubro incorrecto")
        else:
            break
    
    numeros2.decorador(rubro)


def inicio():
    while True:
        preguntar()
        try:
            continuar = input("¿Desea continuar? [S/N]: ").upper()
            if continuar not in "SN":
                raise ValueError
        except ValueError:
            print("Opción incorrecta")
        else:
            if continuar == "N":
                print("Gracias por utilizar la consola de turnos")
                break

inicio()