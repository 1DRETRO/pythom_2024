Descripcion = "Este lapiz azul es de tinta"
Descripcion = Descripcion[:50]
longitud = len(Descripcion) > 50 
print(type(longitud))
descripcion_10 = Descripcion[:10]
print(f"\nDescripción: {Descripcion}")
print(f"¿El tamaño de la cadena descripción es mayor a 50 caracteres? {longitud}")
print(f"Los primeros 10 caracteres de la descripción: {Descripcion_10}")