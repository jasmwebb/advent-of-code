# https://adventofcode.com/2020/day/8

from copy import deepcopy


def run_instructions(instructions: list):
    """Runs through given instructions exactly one time.
    Terminates and returns True with a list of possible corrupted operations
    when it encounters an infinite loop.
    Returns value of accumulator at time of terimation.
    """
    acc, i, executed, verify = 0, 0, [], []

    while i < len(instructions):
        if i in executed:
            return (True, acc, verify)
        else:
            op, arg = instructions[i]
            executed.append(i)

            if op == "acc":
                acc += arg
            else:  # "nop" or "jmp"
                verify.insert(0, i)

                if op == "jmp":
                    i += arg
                    continue

            i += 1

    return (False, acc)


def verify_corrupt(instructions: list):
    """Finds the corrupt operation in a list of possible corrupted operation
    indicies, repairs it, and reruns instructions.
    """
    corrupted, acc, corrupt_ops = run_instructions(instructions)
    swap = {"nop": "jmp", "jmp": "nop"}
    rerun = (corrupted, acc)

    if corrupted:
        for op in corrupt_ops:
            instr_copy = deepcopy(instructions)
            instr_copy[op][0] = swap[instructions[op][0]]
            rerun = run_instructions(instr_copy)

            if not rerun[0]:
                break

    return rerun


if __name__ == "__main__":
    with open("input.txt", "r") as inputf:
        boot_code = (line.split() for line in inputf)
        boot_code = [[op, int(arg)] for op, arg in boot_code]

    print(f"Part 1: {run_instructions(boot_code)[1]}")  # 1797
    print(f"Part 2: {verify_corrupt(boot_code)[1]}")  # 1036
