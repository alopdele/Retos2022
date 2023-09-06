"""
 * Reto #25
 * PIEDRA, PAPEL, TIJERA
 * Fecha publicación enunciado: 20/06/22
 * Fecha publicación resolución: 27/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
 """
def piedra_papel_tijera(arr):
    jugador1 = 0
    jugador2 = 0
    for partida in arr:
        if partida[0] != partida[1]:
            if partida[0] == "P" and partida[1] == "R":
                jugador1 += 1
            elif partida[0] == "R" and partida[1] == "S":
                jugador1 += 1
            elif partida[0] == "S" and partida[1] == "P":
                jugador1 += 1
            else:
                jugador2 += 1

    if jugador1 == jugador2:
        return "Tie"
    elif jugador1 > jugador2:
        return "Player 1"
    else:
        return "Player 2"


print(piedra_papel_tijera([("R","S"), ("S","R"), ("P","S")]))    

