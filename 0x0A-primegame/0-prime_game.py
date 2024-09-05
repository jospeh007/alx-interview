#!/usr/bin/python3
"""Prime Game Module"""

def isWinner(x, nums):
    """
    Determines the victor of a series of prime number elimination games.

    Args:
        x (int): Number of rounds to be played.
        nums (list of int): List of integers, each representing a set of
        consecutive integers from 1 to n.

    Returns:
        str: The name of the player who won the most rounds ("Ben" or "Maria").
        None: If there’s no clear winner.

    Raises:
        None.
    """
    # Validate input parameters
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    # Set up scores for both players
    ben = 0
    maria = 0
    # Initialize a list 'a' with values 1 for all indices up to the maximum number
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    # Mark indices 0 and 1 as non-prime (0) as these are not prime numbers
    a[0], a[1] = 0, 0
    # Apply the Sieve of Eratosthenes to mark non-prime indices
    for i in range(2, len(a)):
        rm_multiples(a, i)
    # Simulate each round of the game
    for i in nums:
        # If the sum of primes up to i is even, Ben wins the round
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # Determine the overall winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None

def rm_multiples(ls, x):
    """
    Marks the multiples of a prime number as non-prime in a list.

    Args:
        ls (list of int): List representing potential prime numbers.
        x (int): The prime number whose multiples are to be marked.

    Returns:
        None.

    Raises:
        None.
    """
    # Iterate over multiples of the prime number and mark them as non-prime
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break

