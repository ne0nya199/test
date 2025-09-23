import math

""" SecondTask: """


def tableEquation(a, b, step ):

    start_int = int(a * 100)
    end_int = int(b * 100)
    step_int = int(step * 100)

    for i in range(start_int, end_int, step_int):
        x = i / 100.0
        y = (x ** (1 / (2 * x))) + ((x ** 2) * math.log((x ** 3))) / ((math.sin(x) ** 2) + (math.cos(x) ** 2))
        print("x: ", x)

tableEquation(0.1, 1.5,0.05)
