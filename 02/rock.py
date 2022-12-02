f = open('input.txt', 'r').read()

rock_01 = f.splitlines()

e = open('example.txt', 'r').read()

rock_00 = e.splitlines()

def score(input):
    parsed = [
        game.split()
        for game in input
    ]
    result = 0

    for round in parsed:
        if round[1] == 'Y':
            result+=2
            if round[0] == 'A':
                result+=6
            if round[0] == 'B':
                result+=3
        if round[1] == 'X':
            result+=1
            if round[0] == 'C':
                result+=6
            if round[0] == 'A':
                result+=3
        if round[1] == 'Z':
            result+=3
            if round[0] == 'B':
                result+=6
            if round[0] == 'C':
                result+=3

    return result

def score2(input):
    parsed = [
        game.split()
        for game in input
    ]
    result = 0

    for round in parsed:
        if round[1] == 'Z':
            result+=6
            if round[0] == 'A':
                result+=2
            if round[0] == 'B':
                result+=3
            if round[0] == 'C':
                result+=1
        if round[1] == 'Y':
            result+=3
            if round[0] == 'A':
                result+=1
            if round[0] == 'B':
                result+=2
            if round[0] == 'C':
                result+=3
        if round[1] == 'X':
            if round[0] == 'A':
                result+=3
            if round[0] == 'B':
                result+=1
            if round[0] == 'C':
                result+=2

    return result


print(score(rock_00))
print(score(rock_01))

print(score2(rock_00))
print(score2(rock_01))