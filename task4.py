import math

"""work with func"""
def tableOfSum():
    num = 1
    sum = 0

    while num < 50:
        sum += (2.2 ** ((2 * num) + 1)) / (math.factorial((2 * num) + 1))
        num += 1
    return "sum: ", round(sum, 3)

print(tableOfSum())


"""interaction with user"""

def tableOfSumWithUser(num = int(input())):
    sum = 0

    while num < 50:
        sum += (2.2 ** ((2 * num) + 1)) / (math.factorial((2 * num) + 1))
        num += 1
    print("sum: ", round(sum, 3))

tableOfSumWithUser()
