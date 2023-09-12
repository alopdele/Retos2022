"""
#   Reto #28
#   MÁQUINA EXPENDEDORA
#   Fecha publicación enunciado: 11/07/22
#   Fecha publicación resolución: 18/07/22
#   Dificultad: MEDIA
#
#   Enunciado: Simula el funcionamiento de una máquina expendedora creando una operación
#   que reciba dinero (array de monedas) y un número que indique la selección del producto.
#   - El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor
#     número de monedas).
#   - Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un mensaje
#     y retornar todas las monedas.
#   - Si no hay dinero de vuelta, el array se retornará vacío.
#   - Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
#   - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
"""

# Productos de la máquina expendedora
PRODUCTS = {
    1: {"name": "Coca-Cola 350 ml", "price": 150},
    2: {"name": "Coca-Cola 500 ml", "price": 250},
    3: {"name": "Milk 120 ml", "price": 120},
    4: {"name": "Pizza small", "price": 500},
    5: {"name": "Sandwich", "price": 420},
    6: {"name": "Cereal", "price": 80},
    7: {"name": "Chocolate", "price": 360},
    8: {"name": "Water 500 ml", "price": 200},
    9: {"name": "Candy", "price": 30},
    10: {"name": "Yogurth", "price": 70}
}

# Monedas soportadas
COINS = [200, 100, 50, 10, 5]


def cashback_coins(cashback: int):
    coin_return = []
    cashback_total = cashback
    index = 0

    while cashback_total > 0:
        value_coin = COINS[index]

        if cashback_total >= value_coin:
            cashback_total -= value_coin
            coin_return.append(value_coin)

        if cashback_total < value_coin:
            index += 1

    return coin_return


def expendor_machine(coins: list[int], item: int):

    # Define si el producto está disponible en la máquina y el formato de las monedas ingresadas es correcto
    product_available = True if item in PRODUCTS.keys() else False
    coins_allowed = True
    [coins_allowed := False for coin in coins if coin not in COINS]

    if product_available and coins_allowed:
        # Obtiene el precio y nombre del producto
        product_item = PRODUCTS.get(item)
        product_price = product_item.get("price")
        product_name = product_item.get("name")

        # Define el total de monedas ingresadas
        total_cash = 0

        for coin in coins:
            total_cash += coin

        # Define si se tiene el dinero necesario para comprar
        if total_cash >= product_price:

            # Define la diferencia de dinero como cashback
            cashback = total_cash - product_price

            # Imprime la
            print(f"Retire '{product_name}' del dispensador.")

            if cashback == 0:
                print("No hay vuelto. Gracias por su compra!\n")

            else:
                # Determina las monedas a retornar
                cashback_moneys = cashback_coins(cashback)
                print(
                    f"Aquí está su vuelto {cashback_moneys}. Gracias por su compra!\n")

        else:
            # Define respuestas para
            print(
                f"Faltan {product_price - total_cash} centavos para comprar '{product_name}'.")
            print(f"Sus monedas {coins} son devueltas.\n")

    else:
        print("La opción ingresada no existe o no fueron ingresadas monedas permitidas\n")


# Tests
# (1)
expendor_machine(coins=[5, 10], item=9)

# (2)
expendor_machine(coins=[5, 100, 200], item=7)

# (3)
expendor_machine(coins=[100, 100, 100, 200], item=4)

# (4)
expendor_machine(coins=[100, 100, 100, "200"], item=4)

# (5)
expendor_machine(coins=[100, 100, 100, 200], item=23)


# Result Tests
# (1)
# Faltan 15 centavos para comprar 'Candy'.
# Sus monedas [5, 10] son devueltas.
#
# (2)
# Faltan 55 centavos para comprar 'Chocolate'.
# Sus monedas [5, 100, 200] son devueltas.
#
# (3)
# Retire 'Pizza small' del dispensador.
# No hay vuelto. Gracias por su compra!
#
# (4)
# La opción ingresada no existe o no fueron ingresadas monedas permitidas
#
# (5)
# La opción ingresada no existe o no fueron ingresadas monedas permitidas