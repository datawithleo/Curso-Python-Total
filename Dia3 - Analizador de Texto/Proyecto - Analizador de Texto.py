texto = input("Ingrese un texto: ")
letras = []

texto = texto.lower()
letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("Ingrese la tercera letra: ").lower())

print("\nCANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print("La cantidad de letras", letras[0], "es: ", cantidad_letras1)
print("La cantidad de letras", letras[1], "es: ", cantidad_letras2)
print("La cantidad de letras", letras[2], "es: ", cantidad_letras3)

print("\nCANTIDAD DE PALABRAS")
palabras = texto.split()
print("La cantidad de palabras es: ", len(palabras))

print("\nLETRAS DE INICIO Y FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print("La letra de inicio es: ", letra_inicio)
print("La letra final es: ", letra_final)

print("\nTEXTO INVERTIDO")
palabras.reverse()
texto_invertido = " ".join(palabras)
print("El texto invertido es: ", texto_invertido)

print("\nBUSCANDO LA PALABRA PYTHON")
buscar_python = "python" in texto
dic = {True: "SI", False: "NO"}
print("¿Existe la palabra python en el texto?", dic[buscar_python])