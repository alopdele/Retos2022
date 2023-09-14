"""
 * Reto #30
 * MARCO DE PALABRAS
 * Fecha publicación enunciado: 26/07/22
 * Fecha publicación resolución: 01/08/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba un texto y muestre cada palabra en una línea, formando
 * un marco rectangular de asteriscos.
 * - ¿Qué te parece el reto? Se vería así:
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********
 """
def dibujarCuadrado(cadena:str):
    palabras = cadena.split(" ")
    longitud_maxima = 0
    for palabra in palabras:
        if len(palabra) > longitud_maxima:
            longitud_maxima = len(palabra)       

    techo = longitud_maxima + 4
    print(techo)

    print("*" * techo)
    for palabra in palabras:
        if palabra != "":
            espacios = " " * (techo - len(palabra) - 4 )
            print(f"* {palabra}{espacios} *")
    print("*" * techo)

dibujarCuadrado("¿Qué te parece el reto?")
dibujarCuadrado("¿Qué te     parece el reto?")
dibujarCuadrado("¿Cuántos retos de código de la comunidad has resuelto?")