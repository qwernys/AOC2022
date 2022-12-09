def findStartOfPacket(path):
    file = open(path)
    i = 0
    recentFour = [0,0,0,0]
    while True:
        i += 1
        c = file.read(1)
        if not c:
            break
        recentFour[i % 4] = c
        if i > 3:
            if len(set(recentFour)) == 4:
                return i

def findStartOfPacket2(path):
    file = open(path)
    i = 0
    recentFour = [0 for _ in range(14)]
    while True:
        i += 1
        c = file.read(1)
        if not c:
            break
        recentFour[i % 14] = c
        if i > 13:
            if len(set(recentFour)) == 14:
                return i
        
i = findStartOfPacket2("/Users/kevinjonsson/Documents/Python/AOC2022/Day 6/input.txt")
print(i)