# https://adventofcode.com/2020/day/8


def run_instructions(instructions: list) -> int:
    """Run through given instructions exactly one time.
    Returns value of accumulator at time of terimation.
    """
    instr = instructions
    acc, i, executed = 0, 0, []

    while i < len(instr):
        if i in executed:
            break
        else:
            op, arg = instr[i]
            executed.append(i)

            if op == "acc":
                acc += arg
            elif op == "jmp":
                i += arg
                continue

            i += 1

    return acc


if __name__ == "__main__":
    with open("test.txt", "r") as inputf:
        boot_code = (line.split() for line in inputf)
        boot_code = [[op, int(arg)] for op, arg in boot_code]

    print(f"Part 1: {run_instructions(boot_code)}")  # 1797
