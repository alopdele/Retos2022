"""
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
 *
 *
"""
from collections import Counter

#lo voy a hacer de la forma rapida
def contarPalabras(texto):
    #Podriamos quitar los simbolos de puntuación con replace
    texto = texto.lower()
    conteo = Counter(texto.split(" "))
    return conteo

print(contarPalabras("hola que ase , ."))