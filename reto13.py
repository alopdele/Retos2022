"""
 * Reto #13
 * FACTORIAL RECURSIVO
 * Fecha publicación enunciado: 28/03/22
 * Fecha publicación resolución: 04/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n+1):
            resultado = resultado * i
        return resultado
    

print(factorial(5))


##Podriamos usar recursividad para resolverlo

def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo (n-1)
    
print(factorial_recursivo(5))