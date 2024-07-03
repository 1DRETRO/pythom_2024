# Tupla de ejemplo
tupla = (1, 2, 3, 2, 4, 5, 1, 6, 1)

# Crear un diccionario para contar las ocurrencias
conteo = {}

# Contar las ocurrencias de cada elemento en la tupla
for item in tupla:
    if item in conteo:
        conteo[item] += 1
    else:
        conteo[item] = 1

# Imprimir los valores duplicados
duplicados = [item for item, count in conteo.items() if count > 1]

print("Valores duplicados:", duplicados)
