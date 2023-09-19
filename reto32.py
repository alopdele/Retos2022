"""
 * Reto #32
 * EL SEGUNDO
 * Fecha publicación enunciado: 08/08/22
 * Fecha publicación resolución: 15/08/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Dado un listado de números, encuentra el SEGUNDO más grande.
 """

def segundoMasGrande(lista: list):
    if len(lista)>2:
        lis = sorted(lista, reverse=True)
        print(lis)
        return lis[1]
    else:
        return "La lista tiene menos de dos elementos"
    
print(segundoMasGrande([2,6,3,5,7,9,0,1]))