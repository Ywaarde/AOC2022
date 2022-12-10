def pixel(cycle, signal):
    if (cycle%40) in [signal-1, signal, signal+1]:
        return '#'
    else:
        return ' '

def display(input):
    cycle = 0
    signal = 1
    crt = []
    
    for line in input:
        p_line = line.split(' ')
        if p_line[0] == 'noop':
            crt.append(pixel(cycle, signal))
            cycle+=1
        else:
            crt.append(pixel(cycle, signal))
            cycle+=1
            crt.append(pixel(cycle, signal))
            cycle+=1
            signal += int(p_line[1])
    
    # print(crt)
    for i in range(6):
        print(''.join(crt[i*40:(i+1)*40]))
    

def strength(input):
    result = 0
    cycle = 0
    signal = 1
    intervals = range(20, 221, 40)
    for line in input:
        p_line = line.split(' ')
        if p_line[0] == 'noop':
            cycle+=1
            if cycle in intervals: 
                result += (signal*cycle)
        else:
            cycle+=1
            if cycle in intervals: 
                result += (signal*cycle)
            
            cycle+=1
            if cycle in intervals: 
                result += (signal*cycle)
            signal += int(p_line[1])
    
    return result




cycles_00 = open('example.txt', 'r').read().splitlines()
cycles_01 = open('input.txt', 'r').read().splitlines()

print('part 1')
print('example')
print(strength(cycles_00))
print('puzzle')
print(strength(cycles_01))


print('part 2')
print('example')
print(display(cycles_00))
print('puzzle')
print(display(cycles_01))