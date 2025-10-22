def solution(*args):
    frog = [1, 1, 1]
    y = 0
    z = 0
    for x in range(len(args)):
        frog[1] = args[y]
        frog[0] += frog[1]
        y += 1; z += 1
        frog[2] = z
        print(frog, z,)
        if frog[2] > len(args):
            return -1
    return frog[2]

print(solution(1, 2, 2, -1))
