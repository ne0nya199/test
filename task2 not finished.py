import math

""" SecondTask: """

a = 15
b = 1
step = 0


for x in range(b, a, step):
    y = (x ** (1 / (2 * x))) + ((x ** 2) * math.log((x ** 3))) / ((math.sin(x) ** 2) + (math.cos(x) ** 2))
