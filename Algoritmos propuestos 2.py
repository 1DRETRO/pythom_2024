Descripcion = "Este lapiz es azul tinta"
Descripcion = Descripcion[:50] 
Longitud = len(Descripcion) > 50 

Descrip_10 = Descripcion[:10]

print(f"Descripción: {Descripcion}")
print(f"¿El tamaño de la cadena descripción es mayor a 50 caracteres? {Longitud}")
print(f"Los primeros 10 caracteres de la descripción: {Descrip_10}")