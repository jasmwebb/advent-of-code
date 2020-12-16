# https://adventofcode.com/2020/day/14

from itertools import product


def parse_mask(data):
    """Parses mask from string for both versions of decorder."""
    mask = {i: bit for i, bit in enumerate(data) if bit != "X"}
    mask2 = {i: bit for i, bit in enumerate(data) if bit != "0"}

    return mask, mask2


def decoder_v1(mask, info, data):
    """Emulator for version 1 decoder chip. Uses bitmask to decode value."""
    address = int(info[4:-1])
    value = list(f"{int(data):036b}")

    for i, bit in mask.items():  # Apply bitmask to value
        value[i] = bit

    value = int("".join(value), 2)  # Parse back to int

    return address, value


def decoder_v2(mask, info, data):
    """Emulator for version 2 decoder chip. Uses bitmask to decode address."""
    address = list(f"{int(info[4:-1]):036b}")
    value = int(data)
    floatings = []
    addresses = []

    # Apply bitmask to address, keeping track of floating bit indices
    for i, bit in mask.items():
        address[i] = bit

        if bit == "X":
            floatings.append(i)

    # Generate all possible combinations of values for floating bits
    replacements = product(*((0, 1) for _ in range(len(floatings))))

    for rs in replacements:
        new_address = "".join(address)

        for r in rs:
            new_address = new_address.replace("X", str(r), 1)

        addresses.append(new_address)

    addresses = (int("".join(address), 2) for address in addresses)

    return addresses, value


if __name__ == "__main__":
    filename = "input.txt"
    mem = {}
    mask = {}
    mem2 = {}
    mask2 = {}

    with open(filename, "r") as inputf:
        for line in inputf:
            info, data = line.rstrip().split(" = ")

            if info == "mask":
                mask, mask2 = parse_mask(data)
            else:
                address, value = decoder_v1(mask, info, data)
                mem[address] = value

                addresses, value = decoder_v2(mask2, info, data)

                for address in addresses:
                    mem2[address] = value

    print(f"Part 1: {sum(mem.values())}")  # 3059488894985
    print(f"Part 2: {sum(mem2.values())}")  # 2900994392308
