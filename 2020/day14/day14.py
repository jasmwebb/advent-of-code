# https://adventofcode.com/2020/day/14

if __name__ == "__main__":
    filename = "input.txt"
    mem = {}
    mask = {}

    with open(filename, "r") as inputf:
        for line in inputf:
            info, data = line.rstrip().split(" = ")

            if info == "mask":
                mask = {i: bit for i, bit in enumerate(data) if bit != "X"}
            else:  # info is address in memory
                address = int(info[4:-1])
                value = list(f"{int(data):036b}")

                for i, bit in mask.items():  # Apply bitmask to value
                    value[i] = bit

                value = int("".join(value), 2)  # Parse back to int
                mem[address] = value

    print(f"Part 1: {sum(mem.values())}")  # 3059488894985
