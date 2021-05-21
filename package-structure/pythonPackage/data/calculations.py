import random

def dataCalculation():
    x = range(10)
    y = [random.randrange(100) for _ in x]
    return (x, y)
