from ..data.calculations import dataCalculation
import matplotlib.pyplot as plt

def makeFig():
    x, y = dataCalculation()
    plt.scatter(x,y)
    plt.xlabel("x value")
    plt.ylabel("y value")
    plt.title("title")
