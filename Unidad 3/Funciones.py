#Sirven para reutilizar bloques de codigo, son fuciones personalizadas.
#Pueden aceptar cero o mas argumentos, tiene que ser invocada para imprimir un codigo en especifico.
#Las variables definidas dentro de una funcion son variables locales.
def saludo():
    print("Hola mi nombre es momomo")
    saludo()
import numpy as np
def saludo(nombre):
    print(f"Hola mi nombre es {nombre}")
    saludo("Tomas")