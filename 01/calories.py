f = open('input.txt', 'r').read()

calories_01 = f.splitlines()

e = open('example.txt', 'r').read()

calories_00 = e.splitlines()

def calculate(input):
    max0 = 0
    max1 = 0
    max2 = 0

    amt = 0

    for c in input:
        if c:
            amt = amt + int(c)
        else:
            if amt > max0:
                if max0 > max1:
                    if max1 > max2:
                        max2 = max1
                    max1 = max0
                max0 = amt
            elif amt > max1:
                if max1 > max2:
                    max2 = max1
                max1 = amt
            elif amt > max2:
                max2 = amt
            #     amt = 0
            #     pass
            # if amt > max1:
            #     max1 = amt
            #     amt = 0
            #     pass
            # if amt > max2:
            #     max2 = amt
            #     amt = 0
            #     pass
            amt = 0
    
    return [max0, max1, max2, max0 + max1 + max2]


print(calculate(calories_00))
print(calculate(calories_01))