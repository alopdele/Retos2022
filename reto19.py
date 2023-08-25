"""
 * Reto #19
 * CONVERSOR TIEMPO
 * Fecha publicación enunciado: 09/05/22
 * Fecha publicación resolución: 16/05/22
 * Dificultad: FACIL
 *
 * Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
"""

def time_to_milisecond(days:int, hours: int, minutes: int, second: int):
    dias = days * 24 * 60 * 60 * 1000
    horas = hours * 60 * 60 * 1000
    minutos = minutes * 60 * 1000
    segundos = second * 1000 
    return dias + horas + minutos + segundos

# Tests
print(time_to_milisecond(5, 10, 2, 10))     # -> 468130000
print(time_to_milisecond(20, 50, 90, 500))  # -> 1913900000
print(time_to_milisecond(60, 1, 1, 1))      # -> 5187661000
print(time_to_milisecond(0, 0, 1, 1))       # -> 61000
print(time_to_milisecond(-1, 0, 1, 1))      # -> None
print(time_to_milisecond(0,0,0,10))         # -> 10000
