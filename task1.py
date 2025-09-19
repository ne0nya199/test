import math

def calculate_equation():
    try:

        description = input("input value x: ")
        x = float(description)

        e = math.e

        if (2 + x) <= 0 or (2 - x) <= 0:
            return "Error, ln() need to be positive"

        y = ((e ** (2 * x)) * math.log(2 + x)) - ((2 ** (2 * x)) * math.log(2 - x))
        return f"answer is: {round(y , 5)}"

    except ValueError:
        return "Error, please enter a number"

print(calculate_equation())

# when x equal to 1.5 the answer will be 30.70759
