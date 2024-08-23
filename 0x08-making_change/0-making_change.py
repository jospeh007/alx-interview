#!/usr/bin/python3
""" Coin Change Problem """


def makeChange(coins, total):
    """ Determine the minimum number of coins needed to reach the total amount.

    Args:
        coins (List[int]): List of available coin denominations.
        total (int): The target amount to be achieved using the coins.
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1

