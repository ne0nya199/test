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
            if arrayNums[takenNum] < 0 and takenNum < countOfNums - 1:
                takenNum += 1
                if checkedElement < countOfNums - 1:
                    checkedElement += 1
            else:
                if arrayNums[checkedElement] > 0:
                    if checkedElement < countOfNums - 1:
                        checkedElement += 1
                else:
                    for x in range(countOfNums):
                        if abs(arrayNums[takenNum]) < abs(arrayNums[checkedElement]):
                            print(f"module of element {takenNum}: ", arrayNums[takenNum], f", lesser than module of {checkedElement}: ", arrayNums[checkedElement])
                            if checkedElement != countOfNums - 1:
                                checkedElement += 1
                                while arrayNums[checkedElement] > 0 and checkedElement < countOfNums - 1:
                                    checkedElement += 1
                            else:
                                if takenNum != countOfNums - 1:
                                    takenNum += 1
                                    while arrayNums[takenNum] < 0 and takenNum < countOfNums - 1:
                                        takenNum += 1
                                    if checkedElement != countOfNums - 1 or takenNum != countOfNums - 1:
                                        checkedElement = takenNum + 1
                                    else:
                                        break
                                else:
                                    break
    except ValueError:
        print("Please, enter a number")

checkModule()
