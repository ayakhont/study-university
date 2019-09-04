coins = [25, 10, 5, 1]


def min_coins(number):
    change = []
    for coin in coins:
        if (number >= coin):
            change += [coin] * (number // coin)
            number = number % coin
    return change


print(min_coins(70))