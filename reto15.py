""" 
#  Reto #15
#  ¿CUÁNTOS DÍAS?
#  Fecha publicación enunciado: 11/04/22
#  Fecha publicación resolución: 18/04/22
#  Dificultad: DIFÍCIL
# 
#  Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
#  - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
#  - La función recibirá dos String y retornará un Int.
#  - La diferencia en días será absoluta (no importa el orden de las fechas).
#  - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
"""

from datetime import datetime

def days_between_dates(date1, date2):
    date1 = datetime.strptime(date1, '%d-%m-%Y')
    date2 = datetime.strptime(date2, '%d-%m-%Y')
    delta = date2 - date1
    return delta.days

# Ejemplo de uso
date1 = '12-02-2000'
date2 = '20-02-2020'
difference = days_between_dates(date1, date2)
print(f"Difference in days: {difference}")