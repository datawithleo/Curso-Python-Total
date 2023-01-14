nombre = input("Ingrese su nombre: ")
ventas_totales = int(input("¿Cuántas han sido tus ventas totales?: "))
comision = round(ventas_totales*13/100, 2)

print(f"{nombre} tu comisión es de {comision}")