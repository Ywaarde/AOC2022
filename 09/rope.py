def tail_moves(head, tail):
    # same position
    if head == tail:
        return tail
    # touching side
    if (head[0] == tail[0] and abs(head[1] - tail[1]) == 1 or
        head[1] == tail[1] and abs(head[0] - tail[0]) == 1):
        return tail
    # touching diagonally
    if abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 1:
        return tail
    #  same line
    if head[0] == tail[0]:
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1]-=1
        return tail
    # same collumn
    if head[1] == tail[1]:
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0]-=1
        return tail
    
    if (abs(head[0] - tail[0]) == 2 or abs(head[1] - tail[1]) == 2):
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1

    return tail


def tails(input):
    result = []

    DIR = {
        'L': (-1,0),
        'R': (1,0),
        'U': (0,1),
        'D': (0,-1),
    }

    pos_h = [0,0]
    pos_t = [0,0]

    for move in input:
        p_move = move.split(' ')
        for i in range(int(p_move[1])):
            pos_h[0] += DIR[p_move[0]][0]
            pos_h[1] += DIR[p_move[0]][1]

            pos_t = tail_moves(pos_h, [pos_t[0], pos_t[1]])

            if pos_t not in result:
                result.append(pos_t)

    return len(result)

def nine_tails(input):
    result = []

    DIR = {
        'L': (-1,0),
        'R': (1,0),
        'U': (0,1),
        'D': (0,-1),
    }

    positions = [
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
    ]

    for move in input:
        p_move = move.split(' ')
        for i in range(int(p_move[1])):
            positions[0][0] += DIR[p_move[0]][0]
            positions[0][1] += DIR[p_move[0]][1]

            for i in range(1, len(positions)):
                positions[i] = tail_moves(positions[i-1], [positions[i][0], positions[i][1]])
            


            if positions[9] not in result:
                result.append(positions[9])
    return len(result)

knot_00 = open('example.txt', 'r').read().splitlines()
knot_02 = open('example2.txt', 'r').read().splitlines()
knot_01 = open('input.txt', 'r').read().splitlines()

print('part 1')
print('example')
print(tails(knot_00))
print('puzzle')
print(tails(knot_01))


print('part 2')
print('examples')
print(nine_tails(knot_00))
print(nine_tails(knot_02))
print('puzzle')
print(nine_tails(knot_01))