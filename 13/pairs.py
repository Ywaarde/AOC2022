def right_order(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        if a == b:
            return 0
        if a > b:
            return -1

    if isinstance(a, list) and isinstance(b, list):
        l_a = len(a)
        l_b = len(b)
        s_l = l_a if l_a < l_b else l_b
        for i in range(s_l):
            test = right_order(a[i], b[i])
            if test == 1:
                return 1
            if test == -1:
                return -1
        if l_b > l_a:
            return 1
        elif l_b < l_a:
            return -1
        else:
            return 0

    if isinstance(a, int) and isinstance(b, list):
        return right_order([a], b)

    if isinstance(a, list) and isinstance(b, int):
        return right_order(a, [b])


def bubble_sort(input):
    n = len(input)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if right_order(input[j], input[j + 1]) < 0:
                swapped = True
                input[j], input[j + 1] = input[j + 1], input[j]
        if not swapped:
            return


def order_pairs(input):
    result = 0

    for index, i in enumerate(input):
        ppair = i.split("\n")
        a = eval(ppair[0])
        b = eval(ppair[1])
        test = right_order(a, b)
        if test == 1:
            result += index + 1

    return result


def order_all(input):
    all = []

    for index, i in enumerate(input):
        packets = i.split("\n")
        all.append(eval(packets[0]))
        all.append(eval(packets[1]))

    first = [[2]]
    second = [[6]]
    all.append(first)
    all.append(second)

    bubble_sort(all)

    result2 = []
    for index, i in enumerate(all):
        if i == first:
            result2.append(index + 1)
        if i == second:
            result2.append(index + 1)

    return result2[0] * result2[1]


pairs_00 = open("example.txt", "r").read().split("\n\n")
pairs_01 = open("input.txt", "r").read().split("\n\n")

print("part 1")
print("example")
print(order_pairs(pairs_00))
print("puzzle")
print(order_pairs(pairs_01))

print("part 2")
print("example")
print(order_all(pairs_00))
print("puzzle")
print(order_all(pairs_01))
