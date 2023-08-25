"""
#  Reto #11
#  ELIMINANDO CARACTERES
#  Fecha publicación enunciado: 14/03/22
#  Fecha publicación resolución: 21/03/22
#  Dificultad: FÁCIL
#
#  Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como
#             salida (out1, out2).
#  - out1 contendrá todos los caracteres presentes en la str1, pero NO estén presentes en str2.
#  - out2 contendrá todos los caracteres presentes en la str2, pero NO estén presentes en str1.
#
"""


def delete_common_chars(expr1: str, expr2: str):

    # Define the Output Variables
    out1 = expr1.lower()
    out2 = expr2.lower()

    # List wit common chars between expressions
    chars_in_common = []

    for letra in expr1:
        if letra in expr2 and letra != " ":
            chars_in_common.append(letra)
    #print(chars_in_common)

    for letra in chars_in_common:
        out1 = out1.replace(letra, "")
        out2 = out2.replace(letra, "")        

    print(f"For '{expr1}' the output is: '{out1}'")
    print(f"For '{expr2}' the output is: '{out2}'")


# Tests
delete_common_chars("La justicia", "es armonía.")
delete_common_chars("Si eres bueno para algo", "Nunca lo hagas gratis")
delete_common_chars("La ignorancia", "No es lo mismo que la inocencia.")
delete_common_chars("Siempre tendrás miedo", "A aquello que no entiendas.")

# Result Tests
# delete_common_chars("La justicia", "es armonía.")
#   - For 'La justicia' the output is: 'l jutici'
#   - For 'es armonía.' the output is: 'e rmoní.'
#
# delete_common_chars("Si eres bueno para algo", "Nunca lo hagas gratis")
#   - For 'Si eres bueno para algo' the output is: ' ee be p '
#   - For 'Nunca lo hagas gratis' the output is: 'c  h t'
#
# delete_common_chars("La ignorancia", "No es lo mismo que la inocencia.")
#   - For 'La ignorancia' the output is: ' gr'
#   - For 'No es lo mismo que la inocencia.' the output is: ' es  msm que  e.'
#
# delete_common_chars("Siempre tendrás miedo","A aquello que no entiendas.")
#   - For 'Siempre tendrás miedo' the output is: 'mpr rá m'
#   - For 'A aquello que no entiendas.' the output is: 'a aqull qu  a.'