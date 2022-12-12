def shorter_trees(others, tree):
    for t in others:
        if int(t) >= int(tree):
            return False
    return True


def tree_vis(input, x, y):
    if x == 0 or y == 0:
        return True
    if x == len(input[0]) - 1 or y == len(input) - 1:
        return True

    hor_left = [tree for i, tree in enumerate(input[y]) if i in range(x)]

    hor_right = [
        tree for i, tree in enumerate(input[y]) if i in range(x + 1, len(input[0]))
    ]
    vert_trees = []
    for i in range(len(input)):
        vert_trees.append(input[i][x])
    ver_up = [tree for i, tree in enumerate(vert_trees) if i in range(y)]
    ver_down = [
        tree for i, tree in enumerate(vert_trees) if i in range(y + 1, len(vert_trees))
    ]

    if (
        shorter_trees(hor_left, input[y][x])
        or shorter_trees(hor_right, input[y][x])
        or shorter_trees(ver_up, input[y][x])
        or shorter_trees(ver_down, input[y][x])
    ):
        return True

    return False


def visible(input):
    result = []

    for indey, line in enumerate(input):
        for index, tree in enumerate(line):
            if tree_vis(input, index, indey):
                result.append((index, indey))

    return len(result)


def score_side(tree, others):
    score = 0
    for t in others:
        score += 1
        if int(t) >= int(tree):
            return score
    return score


def score_all(input, x, y):
    if x == 0 or y == 0:
        return 0
    if x == len(input[0]) - 1 or y == len(input) - 1:
        return 0

    hor_left = [tree for i, tree in enumerate(input[y]) if i in range(x)]

    hor_right = [
        tree for i, tree in enumerate(input[y]) if i in range(x + 1, len(input[0]))
    ]
    vert_trees = []
    for i in range(len(input)):
        vert_trees.append(input[i][x])
    ver_up = [tree for i, tree in enumerate(vert_trees) if i in range(y)]
    ver_down = [
        tree for i, tree in enumerate(vert_trees) if i in range(y + 1, len(vert_trees))
    ]

    return (
        score_side(input[y][x], hor_right)
        * score_side(input[y][x], hor_left[::-1])
        * score_side(input[y][x], ver_up[::-1])
        * score_side(input[y][x], ver_down)
    )


def scenic(input):
    result = []

    for indey, line in enumerate(input):
        for index, _ in enumerate(line):
            result.append(score_all(input, index, indey))

    return max(result)


forrest_00 = open("example.txt", "r").read().splitlines()
forrest_01 = open("input.txt", "r").read().splitlines()

print("part 1")
print(visible(forrest_00))
print(visible(forrest_01))


print("part 2")
print(scenic(forrest_00))
print(scenic(forrest_01))
