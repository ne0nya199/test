def checkModuleOfFirstElm():
    try:
        countOfNums = int(input("enter count of numbers: "))
        arrayNums = []
        equalElementsInArray = -1

        for userInteraction in range(countOfNums):
            numsOfUser = int(input())
            arrayNums.append(numsOfUser)

        for x in range(countOfNums):
            if abs(arrayNums[0]) == abs(arrayNums[0 + (x - 1)]):
                x += 1
                equalElementsInArray += 1
        print("number of elements with equal modules (with first value): ", equalElementsInArray)

    except ValueError:
        print("Please, enter a number")


checkModuleOfFirstElm()
