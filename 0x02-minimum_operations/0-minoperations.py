#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n)
""" Return an integer """
    next = 'H'
    body = 'H'
    op = 0
    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            next = body
            body += body
        else:
            op += 1
            body += next
    if len(body) != n:
        return 0
    return op