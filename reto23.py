"""
 * Reto #23
 * MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
 * Fecha publicación enunciado: 07/06/22
 * Fecha publicación resolución: 13/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""


def mcd(numero1: int, numero2: int):
    while numero2 != 0:
        numero1, numero2 = numero2, numero1 % numero2
    print(f"El M.C.D es {numero1}")
    return numero1


def mcm(num1: int, num2: int):
    # Calcula el mcm a partir del mcd y lo imprime
    print(f"El M.C.M de {num1} y {num2} es {(num1*num2) // mcd(num1, num2)}")

mcd(10, 5)
mcd(8, 7)
mcd(1, 2)
mcd(21, 17)

mcm(10, 5)
mcm(8, 7)
mcm(1, 2)
mcm(21, 17)