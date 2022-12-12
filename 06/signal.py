signal_01 = open("input.txt", "r").read()

signal_00 = open("example.txt", "r").read()


def start(input):
    for index, i in enumerate(input):
        if i != input[index + 1] and i != input[index + 2] and i != input[index + 3]:
            if (
                input[index + 1] != input[index + 2]
                and input[index + 1] != input[index + 3]
            ):
                if input[index + 2] != input[index + 3]:
                    return index + 4


def message(input):
    for index, i in enumerate(input):
        if i not in input[index + 1 : index + 14]:
            if input[index + 1] not in input[index + 2 : index + 14]:
                if input[index + 2] not in input[index + 3 : index + 14]:
                    if input[index + 3] not in input[index + 4 : index + 14]:
                        if input[index + 4] not in input[index + 5 : index + 14]:
                            if input[index + 5] not in input[index + 6 : index + 14]:
                                if (
                                    input[index + 6]
                                    not in input[index + 7 : index + 14]
                                ):
                                    if (
                                        input[index + 7]
                                        not in input[index + 8 : index + 14]
                                    ):
                                        if (
                                            input[index + 8]
                                            not in input[index + 9 : index + 14]
                                        ):
                                            if (
                                                input[index + 9]
                                                not in input[index + 10 : index + 14]
                                            ):
                                                if (
                                                    input[index + 10]
                                                    not in input[
                                                        index + 11 : index + 14
                                                    ]
                                                ):
                                                    if (
                                                        input[index + 11]
                                                        not in input[
                                                            index + 12 : index + 14
                                                        ]
                                                    ):
                                                        if (
                                                            input[index + 12]
                                                            not in input[
                                                                index + 13 : index + 14
                                                            ]
                                                        ):
                                                            if (
                                                                input[index + 13]
                                                                not in input[
                                                                    index
                                                                    + 14 : index
                                                                    + 14
                                                                ]
                                                            ):
                                                                return index + 14


def pattern(input, length):
    def rec_find(input, x):
        if len(input) == 1 and x not in input:
            return True

        if x in input:
            return False
        else:
            return rec_find(input[1:], input[0])

    for index, i in enumerate(input):
        if rec_find(input[index + 1 : index + length], input[index]):
            return index + length


print(message(signal_00))
print(message(signal_01))

print(pattern(signal_00, 14))
print(pattern(signal_01, 14))
