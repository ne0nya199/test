import math

"""work with func"""

def tableOfSum():
    num = 1
    mult = 1
    while num <= 15:
        mult *= (((((num ** 4) / 4) + ((num ** 3) / 3) + ((num ** 2) / 2)) + num) / ((3 * (num** 3)) + (2 * (num ** 2)) + num) * math.log(num + 1))
        num += 1
    return  "mult: ", round(mult, 3)

print(tableOfSum())



"""interaction with user"""

def tableOfSum(num = int(input())):
    mult = 1    
    while num <= 15:
        mult *= (((((num ** 4) / 4) + ((num ** 3) / 3) + ((num ** 2) / 2)) + num) / ((3 * (num** 3)) + (2 * (num ** 2)) + num) * math.log(num + 1))
        num += 1
    print("mult: ", round(mult, 3))

tableOfSum()

