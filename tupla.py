#TUPLAS 
Musica = tuple()
generos = ("Rock", "Blues", "Pop", "Metal") #LOS VALORES DE LAS TUPLAS NO SE PUEDEN CAMBIAR 
print(generos)
print(type(generos))
print(generos[3])
print(generos.index("Pop"))

tupla = ("pep", 100, "uni", True)
print(tupla)
tupla = list(tupla)
print(" la tupla ahora es de tipo", type(tupla))
print(tupla[0:3])

conjunto_vacio = set()
conjunto_vacio1 = {"dididid"} #LAS LLAVES SIRVEN PARA SETS Y DICCIONARIOS 

print(type(conjunto_vacio))
print(type(conjunto_vacio1))

