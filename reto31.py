"""
* Reto #31
 * AÑOS BISIESTOS
 * Fecha publicación enunciado: 01/08/22
 * Fecha publicación resolución: 08/08/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio.

 """
 # Condicion bisiesto: (currentYear % 4 == 0 && (currentYear % 100 != 0 || currentYear % 400 == 0)) 

def bisiestos(año: int):
    añoActual = año
    contador = 0
    while (contador<30):
        if añoActual % 4 == 0 and (añoActual % 100 != 0 or añoActual% 400 == 0):
            print(añoActual)
            contador += 1
        añoActual += 1

bisiestos(2000)