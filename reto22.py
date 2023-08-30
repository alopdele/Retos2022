"""
#  Reto #22
#  CONJUNTOS
#  Fecha publicación enunciado: 01/06/22
#  Fecha publicación resolución: 07/06/22
#  Dificultad: FÁCIL
#
#  Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
#  - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
#  - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
#  - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

def compare_list(list_one: list, list_two: list, compare: bool):
    #Lista con los comunes
    comunes = [i for i in list_one if i in list_two]
    #Lista no comunes
    noComunes = [i for i in list_one if i not in list_two]
    noComunes.extend([i for i in list_two if i not in list_one])
    #return
    return comunes if compare else noComunes

# Tests
print(compare_list([1, 2, 3], [3, "4", 5], True))
print(compare_list([1, 2, 3], [3, "4", 5], False))
print(compare_list([1, "g", "3", 6, 7], ["3", "g", 5], True))
print(compare_list([1, "g", "3", 6, 7], ["3", "g", 5], False))
print(compare_list([1, 2, 3], [3, 4, 5, 8, 9], True))
print(compare_list([1, 2, 3], [3, 4, 5, 8, 9], False))

# Result Test
# [1, 2, 3], [3, "4", 5], False             -> [3]
# [1, 2, 3], [3, "4", 5], True              -> [1, 2, '4', 5]
# [1, "g", "3", 6, 7], ["3", "g", 5], True  -> ['g', '3']
# [1, "g", "3", 6, 7], ["3", "g", 5], False -> [1, 6, 7, 5]
# [1, 2, 3], [3, 4, 5, 8, 9], True          -> [3]
# [1, 2, 3], [3, 4, 5, 8, 9], False         -> [1, 2, 4, 5, 8, 9]

#Una alternativa para resolverlo directamente es convertir las listas a set y hacer la interseccion para sacar los comunes 
def comparar_lista(list_one:list, list_two: list, compare:bool):
    set1 = set(list_one)
    set2 = set(list_two)
    comunes = set1.intersection(set2)
    noComunes = set1.symmetric_difference(set2)
    return list(comunes) if compare else list(noComunes)

print(comparar_lista([1, 2, 3], [3, "4", 5], True))
print(comparar_lista([1, 2, 3], [3, "4", 5], False))
print(comparar_lista([1, "g", "3", 6, 7], ["3", "g", 5], True))
print(comparar_lista([1, "g", "3", 6, 7], ["3", "g", 5], False))
print(comparar_lista([1, 2, 3], [3, 4, 5, 8, 9], True))
print(comparar_lista([1, 2, 3], [3, 4, 5, 8, 9], False))