import time

"""
 * Reto #20
 * PARANDO EL TIEMPO
 * Fecha publicación enunciado: 16/05/22
 * Fecha publicación resolución: 23/05/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa principal. Se podría ejecutar varias veces al mismo tiempo.
"""
import asyncio

async def suma(valor1: int, valor2: int, espera: int):
    await asyncio.sleep(espera)
    print(valor1 + valor2)
    return valor1 + valor2

async def main():
    await asyncio.gather(
        suma(10, 10, 5),
        suma(5, 5, 2),
        suma(15, 15, 10)
    )

asyncio.run(main())
