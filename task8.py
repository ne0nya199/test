flashDrive = ["110 mb"]
strLaptop = [150, 17, 18, 19 , 100]
userLaptop = []

def copyFiles():
    int_b = int(flashDrive[0].replace(' mb', ''))
    initialValue = int_b; indexOfnum = 0
    for x in range(len(strLaptop)):
        if int_b >= strLaptop[indexOfnum]:
            flashDrive.append(strLaptop[indexOfnum])
            int_b -= strLaptop[indexOfnum]
            strLaptop.remove(strLaptop[indexOfnum])
        else:
            indexOfnum += 1
    flashDrive[0] = flashDrive[0].replace(str(initialValue), str(int_b))
    print("u have: ", flashDrive[0], "| ur folders:", flashDrive[1: len(flashDrive)], "| remaining folders on pc: ", strLaptop)


def pasteFiles():
    int_b = int(flashDrive[0].replace(' mb', ''))
    initialValue = int_b
    for x in range(1, len(flashDrive)):
            userLaptop.append(flashDrive[1])
            int_b += flashDrive[1]
            flashDrive.remove(flashDrive[1])
    flashDrive[0] = flashDrive[0].replace(str(initialValue), str(int_b))
    print("u have: ", flashDrive[0], "| ur folders:", flashDrive[1: len(flashDrive)], "| remaining folders on your pc: ", userLaptop)

copyFiles()
pasteFiles()
copyFiles()
pasteFiles()
