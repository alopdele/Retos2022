"""
* Challenge #6
* REVERSING STRINGS
* Difficulty: EASY
*
* Reto #6
* INVIRTIENDO CADENAS
* Dificultad: FÁCIL
*
* Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
* - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def rapida(cadena):
    return cadena[::-1]

def lenta(cadena):
    lon = len(cadena) -1
    invertida = ""
    for letra in cadena:
        invertida = invertida + cadena[lon]
        lon = lon -1
    return invertida



print(rapida("Hola mundo"))
print(lenta("Hola mundo")) 