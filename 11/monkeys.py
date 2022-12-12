def parse_monkeys(input):
    result = {}
    global_test = 1

    for monkey in input:
        lines = monkey.splitlines()
        items = lines[1].strip().split(":")
        operation = lines[2].strip().split(" ")
        test = lines[3].strip().split(" ")
        global_test *= int(test[-1])
        single_monkey = {
            "items": [int(i) for i in items[1].split(",")],
            "operation": {
                "operator": operation[-2],
                "modifier": int(operation[-1]) if operation[-1].isnumeric() else "x",
            },
            "test": {
                "factor": int(test[-1]),
                "true": int(lines[4].strip().split(" ")[-1]),
                "false": int(lines[5].strip().split(" ")[-1]),
            },
        }
        result[int(lines[0][:-1].split(" ")[1])] = single_monkey

    return result, global_test


def count(input, rounds, part):

    monkey_index, global_test = parse_monkeys(input)

    result = [0 for _ in range(len(monkey_index.keys()))]

    for _ in range(rounds):
        for m in monkey_index.keys():
            for i in monkey_index[m]["items"]:
                worry_level = i
                if monkey_index[m]["operation"]["operator"] == "+":
                    worry_level += (
                        monkey_index[m]["operation"]["modifier"]
                        if monkey_index[m]["operation"]["modifier"] != "x"
                        else worry_level
                    )
                else:
                    worry_level *= (
                        monkey_index[m]["operation"]["modifier"]
                        if monkey_index[m]["operation"]["modifier"] != "x"
                        else worry_level
                    )
                if part == 1:
                    worry_level = worry_level // 3
                elif part == 2:
                    worry_level = worry_level % global_test
                if worry_level % monkey_index[m]["test"]["factor"] == 0:
                    monkey_index[monkey_index[m]["test"]["true"]]["items"].append(
                        worry_level
                    )
                else:
                    monkey_index[monkey_index[m]["test"]["false"]]["items"].append(
                        worry_level
                    )
                result[m] += 1
            monkey_index[m]["items"] = []

    return sorted(result)[-2] * sorted(result)[-1]


monkeys_00 = open("example.txt", "r").read().split("\n\n")
monkeys_01 = open("input.txt", "r").read().split("\n\n")

print("part 1")
print("example")
print(count(monkeys_00, 20, 1))
print("puzzle")
print(count(monkeys_01, 20, 1))


print("part 2")
print("example")
print(count(monkeys_00, 10000, 2))
print("puzzle")
print(count(monkeys_01, 10000, 2))
