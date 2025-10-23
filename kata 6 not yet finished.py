def solution(*args):
    frog = [0, 0, 0]
    for x in range(len(args)):
        frog[2] += 1
        frog[1] = args[x]
        # print(frog[1])
        if frog[2] > len(args):
            return -1
    return frog[2]

print(solution(1, 2, 2, -1))
