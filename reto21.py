"""
 * Reto #21
 * CALCULADORA .TXT
 * Fecha publicación enunciado: 23/05/22
 * Fecha publicación resolución: 01/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Lee el fichero "reto21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
 * - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
 
 """
from cmath import nan
import sys

def main():

    myFile ='reto21.txt'

    # Leo fichero, almaceno las líneas en una lista de strings y cierro el fichero
    fichero = open(myFile, 'r')
    Lines = fichero.readlines()
    fichero.close()

    # Variable para almacenar el resultado
    result = 0
    # Variable para almacenar una operación matemática
    data = ''
    # Variable contador
    lineNum = 1
    # Recorro las líneas del fichero
    for line in Lines: 
        # Concateno línea en variable data
        data += line.strip()
        # Por cada 3 líneas tengo una operación matemática
        if (lineNum % 3 == 0):
            #print(data)
            # Almaceno el resultado de la operación matemática
            result = getResult(data)
            # Incluyo el resultado como un elemento más de la lista         
            Lines.insert(lineNum,str(result))
            print(Lines)
            # Vacío data para que sólo tenga una operación matemática
            data=''
        lineNum += 1
    # Redondeo el resultado a 2 decimales
    print(round(result,2))    


def getResult(operation):

    if(operation.count('+') > 0):
        num1,num2 = operation.split('+')
        return (castNumber(num1)+castNumber(num2))
    elif(operation.count('-')):
        elems = operation.split('-')
        # Para control de números negativos
        if len(elems) != 2:
            ind = operation.find('-',1)
            num1 = operation[0:ind]
            num2 = operation[ind+1:]
        else:
           num1,num2 = operation.split('-')
        return (castNumber(num1)-castNumber(num2))
    elif(operation.count('*')):
        num1,num2 = operation.split('*')
        return (castNumber(num1)*castNumber(num2))
    elif(operation.count('/')):
        num1,num2 = operation.split('/')
        return (castNumber(num1)/castNumber(num2))
    else:
        sys.exit(f'No se han podido resolver las operaciones. Error en: {operation}')

def castNumber(numString):
    try:
        return float(numString)
    except:
        sys.exit(f'No se han podido resolver las operaciones. Error obteniendo número de: {numString}')


if __name__ == '__main__':
    main()