"""
 * Reto #16
 * EN MAYÚSCULA
 * Fecha publicación enunciado: 18/04/22
 * Fecha publicación resolución: 25/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
 *
"""
def mayus(string):
    cadena = [palabra[0].upper() + palabra[1::].lower() for palabra in string.split(" ")]
    cadena2 = " ".join(cadena)
    print(cadena2)
    
mayus("hola que ase")