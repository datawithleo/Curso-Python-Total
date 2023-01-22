from random import randint

intentos = 0  # Contador de intentos
numero = 0  # Número ingresado por el jugador
numero_secreto = randint(1, 100)  # Genera un número aleatorio entre 1 y 100
nombre = input("¿Cómo te llamas?: ")  # Pide el nombre del jugador

print(f"¡Hola {nombre}! Estoy pensando en un número entre 1 y 100.\nIntenta adivinarlo.\nTienes 8 intentos.")

while intentos < 8:  # Mientras el contador de intentos sea menor que 8
    numero = int(input("Ingresa un número: "))  # Pide un número
    intentos += 1  # Suma 1 al contador de intentos
    if numero not in range(1, 101):  # Si el número ingresado no está entre 1 y 100
        print("El número debe estar entre 1 y 100")   
    elif numero == numero_secreto:  # Si el número ingresado es igual al número secreto
        print(f"¡Felicidades {nombre}! ¡Adivinaste el número en {intentos} intentos!")
        break  # Rompe el ciclo
    elif numero < numero_secreto:  # Si el número ingresado es menor al número secreto
        print("El número es mayor")
    elif numero > numero_secreto:  # Si el número ingresado es mayor al número secreto
        print("El número es menor")

if numero != numero_secreto:  # Si el número ingresado no es igual al número secreto
    print(f"¡Lo siento {nombre}! No adivinaste el número. El número secreto era {numero_secreto}.")