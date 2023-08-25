"""
 * Reto #14
 * ¿ES UN NÚMERO DE ARMSTRONG?
 * Fecha publicación enunciado: 04/04/22
 * Fecha publicación resolución: 11/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
 Un numero es Amstrong si la suma de sus digitos elevados a la potencia de su numero de cifras es igual al numero en si
 """
def armstrong(numero):
    suma = 0
    longitud = len(str(numero))
    numerostr = str(numero)

    for digito in numerostr:
        suma = suma + int(digito) ** longitud
    print(suma)
    return numero == suma

llamada = armstrong(153)
print(llamada)