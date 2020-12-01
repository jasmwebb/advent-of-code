from itertools import permutations


def read_codes(ints):
    """ Reads through intcode program, yielding on instruction at a time.
    Moves instruction pointer by number of values in the instruction (4).
    """
    for pointer in range(0, len(ints), 4):
        yield ints[pointer:pointer + 4]


def process_codes(instructions):
    """ Read opcode and processes values accordingly.
    1: add values at positions specified by 2nd and 3rd values, then write sum
    at position specified by 4th value
    2: same as opcode 1, but with multiplications rather than addition
    99: terminate program
    """
    for instruction in instructions:
        opcode = instruction[0]
        param1 = instruction[1]
        param2 = instruction[2]
        param3 = instruction[3]

        if opcode == 1:
            intcode[param3] = intcode[param1] + intcode[param2]
        elif opcode == 2:
            intcode[param3] = intcode[param1] * intcode[param2]
        else:
            break


noun_verb_combos = (nv for nv in permutations(range(100), 2))

for nv in noun_verb_combos:
    # Initialize memory to program's values
    with open("input.txt", "r") as inputf:
        intcode = list(map(int, inputf.read().split(",")))

    intcode[1] = nv[0]
    intcode[2] = nv[1]

    instructions = read_codes(intcode)
    process_codes(instructions)

    if intcode[0] == 19690720:
        print(100 * intcode[1] + intcode[2])
        break
