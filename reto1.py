"""
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
"""
#Esto es una forma de hacerlo. Ponemos la palabra en minuscula. Y hacemos la comprabación de que todas las letras esten en las dos palabras

def anagrama (palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    if palabra1 == palabra2:
        return "No son anagramas. Son la misma palabra"
    if len(palabra1) != len(palabra2):
        return "No son anagramas. La longitud de las palabras no es la misma"
    for letra in palabra1:
        if letra in palabra2:         
            palabra2.replace(letra, "")
        else:
            return False
    return True

print(anagrama("barcu", "bbbbb"))
    
#Otra forma más simple y tal vez mas correcta. Formar dos listas, cada una sea la palabra comprobar si esas listas una vez ordenadas son iguales

def anagrama2 (palabra1,palabra2):
    palabra1 = list(palabra1.lower())
    palabra2 = list(palabra2.lower())
    palabra1.sort
    palabra2.sort
    return palabra1 == palabra2

print(anagrama2("barcu", "bbbbb"))
    