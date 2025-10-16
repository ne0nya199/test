countOffold = int(input("enter count of folder: "))
folds = []

for userInteraction in range(countOffold):
    numsOfUser = str(input("enter a storage of each folders: "))
    folds.append(numsOfUser + " мб")
print(folds)








int_b = int(folds[0].replace(' мб',''))
print("The integer value",int_b)
