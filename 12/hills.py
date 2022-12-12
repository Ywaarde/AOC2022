from collections import deque


def valid_options(start, input):
    result = []
    x = start[0]
    y = start[1]
    value = input[y][x]

    options = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    for o in options:

        if 0 <= o[1] < len(input) and 0 <= o[0] < len(input[0]):

            maybe = input[o[1]][o[0]]
            if maybe <= value + 1:
                result.append(o)
    return result


#  1  procedure BFS(G, root) is
#  2      let Q be a queue
#  3      label root as explored
#  4      Q.enqueue(root)
#  5      while Q is not empty do
#  6          v := Q.dequeue()
#  7          if v is the goal then
#  8              return v
#  9          for all edges from v to w in G.adjacentEdges(v) do
# 10              if w is not labeled as explored then
# 11                  label w as explored
# 12                  w.parent := v
# 13                  Q.enqueue(w)


def bfs(start, end, height):
    Q = deque()

    Q.append((start, 0))
    explored = set()
    explored.add(start)
    while Q:
        point, distance = Q.popleft()

        if point == end:
            return distance
        for option in valid_options(point, height):
            if option not in explored:
                explored.add(option)
                Q.append((option, distance + 1))


def find_path(input, more=False):

    start = []
    end = []
    # Mapping it because in place evaluating is too hard apparently.
    mapped_input = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]

    for y, line in enumerate(input):
        for x in range(len(line)):
            if line[x] == "S":
                start.append((x, y))
                mapped_input[y][x] = ord("a")
            elif line[x] == "E":
                end = (x, y)
                mapped_input[y][x] = ord("z")
            else:
                if more and line[x] == "a":
                    start.append((x, y))
                mapped_input[y][x] = ord(line[x])

    paths = []
    for s in start:
        p = bfs(s, end, mapped_input)
        if p:
            paths.append(p)

    return sorted(paths)[0]


hills_00 = open("example.txt", "r").read().splitlines()
hills_01 = open("input.txt", "r").read().splitlines()

print("part 1")
print("example")
print(find_path(hills_00))
print("puzzle")
print(find_path(hills_01))


print("part 2")
print("example")
print(find_path(hills_00, True))
print("puzzle")
print(find_path(hills_01, True))
