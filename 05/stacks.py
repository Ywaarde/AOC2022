stacks_01 = open("input_stacks.txt", "r").read().splitlines()

moves_01 = open("input.txt", "r").read().splitlines()

stacks_00 = open("example_stacks.txt", "r").read().splitlines()

moves_00 = open("example.txt", "r").read().splitlines()


def move9000(stacks, moves):
    stack_stacks = get_stacks(stacks)

    for m in moves:
        m_s = m.split()
        times = int(m_s[1])
        source = int(m_s[3]) - 1
        dest = int(m_s[5]) - 1
        for i in range(times):
            crate = stack_stacks[source].pop()
            stack_stacks[dest].append(crate)
    result = ""
    for s in stack_stacks:
        result += s.pop()

    return result


def move9001(stacks, moves):
    stack_stacks = get_stacks(stacks)

    for m in moves:
        m_s = m.split()
        times = int(m_s[1])
        source = int(m_s[3]) - 1
        dest = int(m_s[5]) - 1
        stack_length = len(stack_stacks[source])
        load = stack_stacks[source][(stack_length - times) : stack_length]
        for _ in range(times):
            stack_stacks[source].pop()
        stack_stacks[dest] += load
    result = ""
    for s in stack_stacks:
        result += s.pop()

    return result


def get_stacks(stacks):
    no_stacks = len(stacks[-1].replace(" ", ""))

    stack_stacks = []

    for i in range(no_stacks):
        stack_stacks.append([])

    for i in range(len(stacks) - 2, -1, -1):
        s = 0
        for j in range(1, len(stacks[-1]), 4):
            if stacks[i][j] != " ":
                stack_stacks[s].append(stacks[i][j])
            s += 1
    return stack_stacks


print(move9001(stacks_00, moves_00))
print(move9001(stacks_01, moves_01))
