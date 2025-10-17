countOffold = int(input("enter count of folder: "))
folds = []

for userInteraction in range(countOffold):
    numsOfUser = str(input("enter a storage of each folders: "))
    folds.append(numsOfUser + " мб")
print(folds)



https://drive.google.com/drive/folders/1w5KgUH4gPY60KZkWNZ4D-5W2JDXh45ui?usp=drive_link




int_b = int(folds[0].replace(' мб',''))
print("The integer value",int_b)
