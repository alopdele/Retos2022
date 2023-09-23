"""
 * Reto #34
 * LOS NÚMEROS PERDIDOS
 * Fecha publicación enunciado: 22/08/22
 * Fecha publicación resolución: 29/08/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Dado un array de enteros ordenado y sin repetidos, crea una función que calcule
 * y retorne todos los que faltan entre el mayor y el menor.
 * - Lanza un error si el array de entrada no es correcto.
"""

def numPerdidos(list:int):
    if len(list) < 2:
        return "El array introducido no tiene la longitud correcta"
    else:
        menor = list[0]
        mayor = list[-1]
        perdidos = []
    for i in range(menor,mayor):
        if i not in list:
            perdidos.append(i)
    return perdidos

print(numPerdidos([1,3,4,9]))