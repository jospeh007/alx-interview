#!/usr/bin/python3
""" Coin Change Problem """


def makeChange(coins, total):
    """ Determine the minimum number of coins needed to reach the total amount

    Args:
        coins (List[int]): List of available coin denominations.
        total (int): The target amount to be achieved using the coins.
    """
    if total <= 0:
        return 0
    elif total > 0:
        newList = sorted(coins[:])
        newList = list(reversed(newList))
        count = 0
        value = total + 0
        index = 0
        while value >= 0 and (index < len(newList)):
            if value >= newList[index]:
                value = value - newList[index]
                count += 1
            elif value < newList[index]:
                index += 1
        if index == len(newList):
            if value != 0:
                return -1
            elif value == 0:
                return count
