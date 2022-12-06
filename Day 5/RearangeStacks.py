def GetTopStacks(path):
    file = open(path)
    condition = False
    stacks = [[],[],[],[],[],[],[],[],[]]
    for line in file:
        if not condition:
            if line == "\n":
                condition = True
            else:
                for i in range(9):
                    item = line[1 + i * 4]
                    if item != " ":
                        stacks[i].append(item)
        else:
            instruction = GetInstructions(line)
            move = int(instruction[0])
            frm = int(instruction[1]) - 1
            to = int(instruction[2]) - 1

            move9001(stacks, move, frm, to)
    
    for i in range(len(stacks)):
        print(stacks[i][0], end="")

def move9000(stacks,move,frm,to):
    for i in range(move):
        item = stacks[frm].pop(0)
        stacks[to].insert(0, item)

def move9001(stacks,move,frm,to):
    temp = []
    for i in range(move):
        temp.insert(0, stacks[frm].pop(0))
    for item in temp:
        stacks[to].insert(0, item)

def GetInstructions(line):
    instruction = []
    line = line.replace("\n","")
    instruction = line.split(" ")
    instruction.remove("move")
    instruction.remove("from")
    instruction.remove("to")
    return instruction
        
    
    
# 1   2   3   4   5

GetTopStacks("/Users/kevinjonsson/Documents/Python/AOC2022/Day 5/input.txt")