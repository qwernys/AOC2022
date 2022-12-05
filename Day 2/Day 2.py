#Sten, påse, sax

def GetRoundScore(round):
    score = 0
    if (round[-1] == 'X' and round[0] == 'A') or (round[-1] == 'Y' and round[0] == 'B') or (round[-1] == 'Z' and round[0] == 'C'):
        score += 3

    if round[-1] == 'X':
        if round[0] == 'C':
            score += 6
        score += 1
        
    elif round[-1] == 'Y':
        if round[0] == 'A':
            score += 6
        score += 2
        
    elif round[-1] == 'Z':
        if round[0] == 'B':
            score += 6
        score += 3

    return score

def GetRoundScore2(round):
    score = 0
    
    if round[-1] == 'X':
        if round[0] == 'A':
            score += 3
            
        if round[0] == 'B':
            score += 1
            
        if round[0] == 'C':
            score += 2
        
        score += 0
        
    elif round[-1] == 'Y':
        if round[0] == 'A':
            score += 1
            
        if round[0] == 'B':
            score += 2
            
        if round[0] == 'C':
            score += 3

        score += 3
        
    elif round[-1] == 'Z':
        if round[0] == 'A':
            score += 2
            
        if round[0] == 'B':
            score += 3
            
        if round[0] == 'C':
            score += 1

        score += 6

    return score


def GetTotalScore(file2):
    score = 0
    file = open(file2)
    file = file.read()
    file = file.split("\n")
    #print(file)
    for round in file:
        print(round)
        if round != "":
            score += GetRoundScore2(round)
    
    print(score)

GetTotalScore("/Users/kevinjonsson/Documents/Python/Advent of Code/input")