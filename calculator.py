#https://github.com/Yimo-Liu-13196/lab11-YL-IBD
#Partner 1: Ido Ben David
#Partner 2: Yimo Liu

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    else:
        return math.log(b, a)

def exp(a, b):
    return a ** b