import math

""" SecondTask, work with func """


def tableEquation(a, b, step ):

    start_int = int(a * 100)
    end_int = int(b * 100)
    step_int = int(step * 100)

    for i in range(start_int, end_int, step_int):
        x = i / 100.0
        y = (x ** (1 / (2 * x))) + ((x ** 2) * math.log((x ** 3))) / ((math.sin(x) ** 2) + (math.cos(x) ** 2))
        print("x:", x, "y:", round(y, 5)) # IDK how to write it smooth

tableEquation(0.1, 1.5,0.05)


""" SecondTask, interaction with user: """


def tableEquationUser():
    try:
        a = float(input("input a start of segment (a): "))
        b = float(input("input a end of segment (b): "))
        step = float(input("input a step: "))


        start_int = int(a * 100)
        end_int = int(b * 100)
        step_int = int(step * 100)

        for i in range(start_int, end_int, step_int):
            x = i / 100.0
            y = (x ** (1 / (2 * x))) + ((x ** 2) * math.log((x ** 3))) / ((math.sin(x) ** 2) + (math.cos(x) ** 2))
            print("x:", x, "y:", round(y, 5)) # too

    except ValueError:
        return "wrong index"

print(tableEquationUser())
