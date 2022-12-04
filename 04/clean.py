f = open('input.txt', 'r').read()

ruck_01 = f.splitlines()

e = open('example.txt', 'r').read()

ruck_00 = e.splitlines()

def clean(input):
    result = 0

    for sections in input:
        split = sections.split(',')
        a_s = split[0].split('-')
        b_s = split[1].split('-')

        a = [int(i) for i in a_s ]

        b = [int(i) for i in b_s ]

        if (a[1]-a[0]) > (b[1]-b[0]):
            bigger = a
            smaller = b
        else:
            bigger = b
            smaller = a

        if (bigger[0] <= smaller[0]) and (bigger[1] >= smaller[1]):
            result+=1
    
    return result

def clean2(input):
    result = 0

    for sections in input:
        split = sections.split(',')
        a_s = split[0].split('-')
        b_s = split[1].split('-')

        a = [int(i) for i in a_s ]

        b = [int(i) for i in b_s ]

        for i in range(a[0], a[1]+1):
            if i in range(b[0], b[1]+1):
                result+= 1
                break       
    
    return result

print(clean2(ruck_00))
print(clean2(ruck_01))
