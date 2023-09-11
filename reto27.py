"""
* Reto #27
 * VECTORES ORTOGONALES
 * Fecha publicación enunciado: 07/07/22
 * Fecha publicación resolución: 11/07/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
"""

def vectores_ortogonales(vector1: list, vector2: list):
    producto_escalar = 0
    for elemento in range(len(vector1)):
        producto_escalar += vector1[elemento] * vector2[elemento]
    print(producto_escalar)
    return producto_escalar == 0


vectores_ortogonales([1, 2], [2, 1])
vectores_ortogonales([2, 1], [-1, 2])