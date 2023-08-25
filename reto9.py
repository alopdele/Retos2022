'''
 * Reto #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
'''

def codigo_morse(texto):
    morse = {"A":"·-","B":"-···","C":"-·-·","D":"-··","E":"·","F":"··-·","G":"--·","H":"····",
            "I":"··","J":"·---","K":"-·-","L":"·-··","M":"--","N":"-·","Ñ":"--·--","O":"---",
            "P":"·--·","Q":"--·-","R":"·-·","S":"···","T":"-","U":"··-","V":"···-","W":"·--",
            "X":"-··-","Y":"-·--","Z":"--··","0":"-----","1":"·----","2":"··---","3":"···--",
            "4":"····-","5":"·····","6":"-····","7":"--···","8":"---··","9":"----·","·":"·-·-·-",
            ",":"--··--","?":"··--··",'"':"·-··-·","/":"-··-·", " ":"  "}

    natural = '·-'

    if (texto[0] in natural):
        #Entonces el texto esta en morse
        codigo = texto.split()
        for palabra_en_morse in codigo:
            for clave in morse:
                if morse[clave] == palabra_en_morse:
                    print(clave,end="")
        print(" ")
    else:
        #Entonces esta en codigo natural
        codigo = texto.upper()
        for letra in codigo:
            print(morse.get(letra),end=" ")

def main():
    codigo_morse("··-· · ·-·· ·· --··    -· ·- ···- ·· -·· ·- -··")
    codigo_morse("Feliz Navidad")

main()
