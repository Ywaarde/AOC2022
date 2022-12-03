from operator import itemgetter
from readline import set_completion_display_matches_hook
from signal import siginterrupt


f = open('input.txt', 'r').read()

ruck_01 = f.splitlines()

e = open('example.txt', 'r').read()

ruck_00 = e.splitlines()

def priority(input):
    result = ''

    for sack in input:
        mid = int(len(sack)/2)
        first = sack[:mid]
        second = sack[mid:]
        for fi in first:
            match = next((
                si
                for si in second
                if si == fi
            ), '')
            if match:
                result += match
                break

    return number(result)

def badges(input):
    groups = int(len(input)/3)

    result = ''

    for i in range(groups):
        first_match =''
        for first in input[i*3]:
            match = next((
                second
                for second in input[i*3+1]
                if second == first
            ), '')
            if match not in first_match:
                first_match += match
        for third in input[i*3+2]:
            match = next((
                found
                for found in first_match
                if found == third
            ), '')
            if match:
                result += match
                break
    
    return number(result)

def number(input):
    numeric = 0
    for x in input:
        increase = 0
        lower ='abcdefghijklmnopqrstuvwxyz'
        upper= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if x in lower:
            increase = lower.index(x) + 1
        else:
            increase = (upper.index(x) + 27)
        numeric += increase
    return numeric


print(badges(ruck_00))
print(badges(ruck_01))