def checkModule():
    try:
        countOfNums = int(input("enter count of numbers: "))
        arrayNums = []

        for userInteraction in range(countOfNums):
            numsOfUser = float(input())
            arrayNums.append(numsOfUser)

        takenNum = 0
        checkedElement = 1

        for b in range(countOfNums):
            if arrayNums[takenNum] < 0:
                takenNum += 1
                checkedElement += 1

            else:
                if arrayNums[checkedElement] > 0:
                    if checkedElement < countOfNums - 1:
                        checkedElement += 1
                else:
                    for x in range(takenNum, countOfNums - takenNum):
                        if abs(arrayNums[takenNum]) < abs(arrayNums[checkedElement]):
                            print(f"module of element {takenNum}: ", arrayNums[takenNum], f", lesser than module of {checkedElement}: ", arrayNums[checkedElement])
                            if checkedElement != countOfNums - 1:
                                checkedElement += 1
                                break
                            else:
                                takenNum += 1
                                for nextNum in range(takenNum, countOfNums - 1):
                                    if arrayNums[takenNum] < 0:
                                        takenNum += 1
    except ValueError:
        print("Please, enter a number")

checkModule()
