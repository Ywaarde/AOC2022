import json

def parse_files(input):
    result = {}
    loc = []
    for line in input:
        p_line = line.split(' ')
        if p_line[0] == '$':
            if p_line[1] == 'cd':
                if p_line[2] == '..':
                    loc.pop()
                elif p_line[2] == '/':
                    loc = ['/']
                else:
                    loc.append(p_line[2]+'/')
        else:
            if p_line[0].isnumeric():
                for i in range(len(loc)):
                    target = ''.join(loc[:i+1])
                    if target not in result:
                        result[target] = 0
                    result[target] += int(p_line[0])
    # print(json.dumps(result, indent=4))             
    return result

def smallest(input, free_space):

    parsed_input = parse_files(input)

    req = parsed_input['/'] - (70_000_000 - free_space)

    match = [
        folder
        for folder in parsed_input.values()
        if folder >= req
    ]
    return min(match)

def calc_total(input, max):

    parsed_input = parse_files(input)

    result = 0

    for i in parsed_input.values():
        if i <= max:
            result += i
    
    return result


terminal_00 = open('example.txt', 'r').read().splitlines()
terminal_01 = open('input.txt', 'r').read().splitlines()

print('part 1')
print(calc_total(terminal_00, 100_000))
print(calc_total(terminal_01, 100_000))

print('part 2')
print(smallest(terminal_00, 30_000_000))
print(smallest(terminal_01, 30_000_000))


