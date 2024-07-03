AlturasZC = (8848, 8611, 8586, 8200, 8460, 8200)

AlturasZS = (8848, 5567, 8125, 4560, 8051, 4560) #Se realizan los sets 

AlturasZA = (2200, 2500, 1000, 2200, 3623, 990)

UT = (AlturasZC, AlturasZS, AlturasZA)   #Se unen en una variable

# A)Imprimir los valores duplicados de cada tupla (Utilizando Ciclos)
for zona, alturas in zip(['Central', 'Sur', 'Austral'], [AlturasZC, AlturasZS, AlturasZA]):
    duplicados = [] #La variable y los corchetes se encargan de guardar los valores duplicados de cada zona. 
    for altura in alturas:  # Iterar sobre cada altura en la tupla de alturas de la zona actual
        if alturas.count(altura) > 1 and altura not in duplicados: # Se verifica si la altura aparece más de una vez en la tupla y no está ya en la lista de duplicados
            duplicados.append(altura)  #Se agrega la altura a la lista de duplicados
    print(f"Valores duplicados en Zona {zona}: {tuple(duplicados)}")

# B)Verificar si la altura 8848m se encuentra en las tres tuplas
dato = 8848 in AlturasZC and 8848 in AlturasZS and 8848 in AlturasZA
print(f"8848m está en las tres zonas: {dato}")

newtupla = tuple(set(AlturasZC + AlturasZS + AlturasZA))
print(f"Tupla unida sin duplicados: {newtupla}")

# D)Transformar la tupla obtenida en una lista. Imprimir la nueva lista obtenida
newlista = list(newtupla)
print(f"Lista de alturas: {newlista}")