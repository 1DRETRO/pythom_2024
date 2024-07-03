#INGRESA 150 CARACTERES E IDENTIFICA CUANTAS VECES SE REPITE LA "a".

texto = """Erase una vez, unos niños dichosos del espiritu aventurero. Ese dia, aquel astuto zorro
hambriento por simple avaricia, quizo dar un bocado pese a estar lleno, sus espiritus aun yacen
en aquel oscuro y desolado bosque"""

minusculas = texto.lower()

contador = minusculas.count("a")

print(f"El caracter a se repite {contador} veces")