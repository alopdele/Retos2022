"""
 * Reto #33
 * CICLO SEXAGENARIO CHINO
 * Fecha publicación enunciado: 15/08/22
 * Fecha publicación resolución: 22/08/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un función, que dado un año, indique el elemento y animal correspondiente
 * en el ciclo sexagenario del zodíaco chino.
 * - Información: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
 * - El ciclo sexagenario se corresponde con la combinación de los elementos madera,
 *   fuego, tierra, metal, agua y los animales rata, buey, tigre, conejo, dragón, serpiente,
 *   caballo, oveja, mono, gallo, perro, cerdo (en este orden).
 * - Cada elemento se repite dos años seguidos.
 * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
"""
def zodiacoChino(año:int):
    elementos = ["madera", "fuego", "tierra", "metal", "agua"]
    animales = ["rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "oveja", "mono", "gallo", "perro", "cerdo"]

    if año < 604 :
        return "El ciclo sexagenario comenzó en el año 604."
    
    añoSexagenario = (año - 4) % 60
    elemento = elementos[int((añoSexagenario % 10) / 2)]
    animal = animales[añoSexagenario % 12]

    return f"{añoSexagenario}: {elemento} {animal}"


print(zodiacoChino(1924))
print(zodiacoChino(1946))
print(zodiacoChino(1984))
print(zodiacoChino(604))
print(zodiacoChino(603))
print(zodiacoChino(1987))
print(zodiacoChino(2022))