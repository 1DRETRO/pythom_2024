# Sets
zonacentral = (8848, 8611, 8586, 8200, 8460, 8200)
zonasur = (8848, 5567, 8125, 4560, 8051, 4560)
zonaaustral = (2200, 2500, 1000, 2200, 3623, 990)

# A)Imprimir los valores duplicados de cada tupla (Utilizando Ciclos)
for zona, alturas in zip(['Central', 'Sur', 'Austral'], [zonacentral, zonasur, zonaaustral]):
    duplicados = [] # Lista para guardar los valores duplicados encontrados en cada zona
    for altura in alturas:  # Iterar sobre cada altura en la tupla de alturas de la zona actual
        if alturas.count(altura) > 1 and altura not in duplicados: # Se verifica si la altura aparece más de una vez en la tupla y no está ya en la lista de duplicados
            duplicados.append(altura)  #Se agrega la altura a la lista de duplicados
    print(f"Valores duplicados en Zona {zona}: {tuple(duplicados)}")
    
# A) Otra forma de resolverlo
zonas = ['Central', 'Sur', 'Austral']
for i in range(len(zonas)):
    zona = zonas[i]
    if zona == 'Central':
        alturas = zonacentral
    elif zona == 'Sur':
        alturas = zonasur
    elif zona == 'Austral':
        alturas = zonaaustral

    duplicados = []
    for altura in alturas:
        if alturas.count(altura) > 1 and altura not in duplicados:
            duplicados.append(altura)

    print(f"Valores duplicados en Zona {zona}: {tuple(duplicados)}")

# B)Verificar si la altura 8848m se encuentra en las tres tuplas
dato = 8848 in zonacentral and 8848 in zonasur and 8848 in zonaaustral
print(f"8848m está en las tres zonas: {dato}")

# Otra forma de resolverlo
dato1 = True  # Variable para controlar si 8848 está presente en todas las tuplas
for i in [zonacentral, zonasur, zonaaustral]:  # Iteramos sobre las tuplas
    if 8848 not in i:  # Verificamos si 8848 no está en la tupla actual
        dato1 = False  # Si no está presente, cambiamos el valor de la variable a False
        break  # Salimos del bucle porque ya no es necesario seguir buscando

if dato1:
    print("La altura 8848m está presente en todas las zonas")
else:
    print("La altura 8848m no está presente en todas las zonas")

# Otra forma de resolverlo
altura = 8848
valorEncontrado = False
for zona in [zonacentral, zonasur, zonaaustral]:
    # Se reinicia la variable 'valorEncontrado' al inicio de cada iteración
    valorEncontrado_en_zona = False
    for valor in zona:
        if valor == altura:
            valorEncontrado_en_zona = True
            break
    # Se actualiza la variable 'valorEncontrado' solo si se encuentra en la zona actual
    if valorEncontrado:
        encontra = True
        break
print("\n¿8848m está en todas las tuplas?:", valorEncontrado)

# C)Unir las tuplas en una sola y eliminar los duplicados
newtupla = tuple(set(zonacentral + zonasur + zonaaustral))
print(f"Tupla unida sin duplicados: {newtupla}")

# D)Transformar la tupla obtenida en una lista. Imprimir la nueva lista obtenida
newlista = list(newtupla)
print(f"Lista de alturas: {newlista}")