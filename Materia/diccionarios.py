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

hospital = {"Nombre" : "Augusto Riffart" , "ciudad" : "Castro"}

paciente = dict(
    Nombre = "Francisco",
    edad = "30",
    ciudad = "Castro"
)

doctor = {
    "Nombre" : "Elson",
    "edad" : 40, 
    "Especialidad" : "Cirujano"}

print(paciente, doctor)
doctor.pop("Nombre") #POP ES PARA EXCLUIR CIERTAS VARIABLES AL EJECUTAR EL ALGORITMO 

print(paciente["Nombre"])#ES PARA OBTENER VALORES ESPECIFICOS 

#RECOMENDACION, TRABAJAR SIEMPRE LOS ALGORITMOS CON MINUSCULAS A ESCEPCION DE LO QUE SE MUESTRA AL ESPECTADOR 

paciente.update() #ES PARA ACTUALIZAR VALORES 

paciente.update({
    "ciudad": "Queilen"#ES PARA ACTUALIZAR UN VALOR MAS ESPECIFICO DEL DICCIONARIO
})

paciente.clear() #ES PARA LIMPIAR UN DICCIONARIO DE TODAS LAS CLAVES Y VALORES DE CIERTA VARIABLE
print(paciente)