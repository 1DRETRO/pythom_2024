p = "La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion democratica."
minus = p.lower() #se deja todo en minusculas para poder contar todas las palabras.
r = minus.count("universidad") 
cp = ("universidad",) * r 
print(f"La palabra universidad se repite {r} veces.")
print(f"Las palabras guardadas en la tupla:", cp)