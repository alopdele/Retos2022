"""
 * Reto #24
 * ITERATION MASTER
 * Fecha publicación enunciado: 13/06/22
 * Fecha publicación resolución: 20/06/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno). ¿De cuántas maneras eres capaz de hacerlo? Crea el código para cada una de ellas.
 *
"""
print("----Forma 1: Bucle For ----")
for i in range(1,100):
    print(i)

print("----Forma 2: Bucle while ----")
i = 1
while i < 100:
    print(i)
    i += 1

print("----Forma 3: Compresion de listas ----")
[print(i) for i in range(1,100)]