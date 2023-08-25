"""
 * Reto #8
 * DECIMAL A BINARIO
 * Fecha publicación enunciado: 18/02/22
 * Fecha publicación resolución: 02/03/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 *
"""

def binario_rapido(numero):
    binario = bin(numero)[2:]
    return binario 

def binario_lento(numero):
    binario = ""
    while numero > 1:
        a = int(numero % 2)
        binario = str(a) + binario
        numero = numero /2
    return binario



print(binario_rapido(100))
print(binario_lento(100))